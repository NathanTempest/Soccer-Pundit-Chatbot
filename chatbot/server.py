# server.py
import os, re, json
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

# ---- Optional: pandas for CSV player context ----
import pandas as pd

# ---- Load env (expects OPENAI_API_KEY in .env or environment) ----
load_dotenv()

# --------------- Evergreen mini knowledge base -------------------
KB = """
# Competitions (evergreen overview)
- Premier League: 20 teams, double round-robin (38 matches/team); 3 pts win / 1 draw / 0 loss; tie-breakers primarily GD, then goals.
- La Liga: 20 teams; head-to-head often used before goal difference in many seasons.
- UEFA Champions League: domestic qualification, group stage, then knockout ties (format evolves, but core idea stands: elite European cup).

# Roles & positions
- 4-3-3: wingers give width; #6 anchors; fullbacks overlap or invert.
- 4-2-3-1: double pivot stability; #10 links midfield to striker.
- Pressing: high press vs mid/low blocks; rest defense prevents counters.
- Expected Goals (xG): chance quality metric; separates process from finishing luck.

# Tactical talking points
- Build-up: CBs split, #6 drops; inverted FBs overload midfield.
- Transitions: counter-press “5-second rule”; rest defense (2 CBs + DM).
- Set pieces: outswinger vs inswinger; near-post flick; zonal vs man-marking.

# Common pundit query patterns
- Compare players: role, outputs (G/A for attackers; progressive passes/tackles for mids; aerial duels for CBs), system fit.
- Team struggles: spacing, pressing triggers, rest defense, xG delta (finishing/keeper variance).
- Predictions: probabilities + swing factors (injuries, fatigue, schedule density).
"""

# --------------- Tiny retrieval over KB --------------------------
def retrieve(query: str, kb: str, top_k: int = 6) -> List[str]:
    lines = [l.strip() for l in kb.splitlines() if l.strip()]
    q = query.lower()
    scored = []
    for i, line in enumerate(lines):
        hits = sum(1 for w in re.findall(r"\w+", q) if w in line.lower())
        if hits:
            scored.append((hits, i, line))
    scored.sort(reverse=True)
    return [ln for _, _, ln in scored[:top_k]]

# --------------- Persona / system prompt -------------------------
PUNDIT_SYSTEM_PROMPT = """
You are a charismatic, neutral football TV pundit.
Domains: English Premier League, La Liga, UEFA Champions League.
Tone: confident, analytical, and concise (3–6 tight paragraphs or bullet clusters).
Always:
- Use concrete concepts (4-3-3, #6/#10 roles, pressing triggers, rest defense, xG).
- Separate facts (rules/tactics) from opinions.
- For predictions: give probability ranges + the key swing factors.
- If asked for current/real-time tables/fixtures, clarify they may have changed.
- Keep banter friendly and respectful.
"""

# --------------- Player CSV helpers ------------------------------
PLAYERS_DF = pd.DataFrame()
PLAYER_NAMES_LOWER: List[str] = []
PLAYER_MAP: Dict[str, Dict] = {}

def _safe_load_players(path: str = "players.csv"):
    global PLAYERS_DF, PLAYER_NAMES_LOWER, PLAYER_MAP
    try:
        df = pd.read_csv(path)
        # Normalize types
        for col in ["Goals", "Assists", "PassingAccuracy", "KeyPassesPer90"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        PLAYERS_DF = df.fillna("")
        PLAYER_NAMES_LOWER = [str(n).strip().lower() for n in PLAYERS_DF["Name"].tolist()]
        PLAYER_MAP = {
            str(row["Name"]).strip().lower(): row.to_dict()
            for _, row in PLAYERS_DF.iterrows()
        }
        return True
    except Exception:
        PLAYERS_DF = pd.DataFrame()
        PLAYER_NAMES_LOWER = []
        PLAYER_MAP = {}
        return False

def _format_player_row(d: Dict) -> str:
    # Compact, pundit-friendly line
    return (
        f"{d.get('Name','')} ({d.get('Club','')}, {d.get('League','')}) — {d.get('Position','')} | "
        f"G:{d.get('Goals','')} A:{d.get('Assists','')} Pass%:{d.get('PassingAccuracy','')} "
        f"KP/90:{d.get('KeyPassesPer90','')} | Note: {d.get('StyleNotes','')}"
    )

def find_players_in_text(text: str) -> List[str]:
    """Very simple name spotting: checks if full player names appear in the query."""
    t = " " + text.lower() + " "
    hits = []
    for nm in PLAYER_NAMES_LOWER:
        # Match whole name roughly (avoid substrings inside words)
        if f" {nm} " in t or t.strip().endswith(nm) or t.strip().startswith(nm):
            hits.append(nm)
    # Deduplicate while preserving order
    seen = set()
    out = []
    for h in hits:
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out

def build_player_context(query: str) -> str:
    if PLAYERS_DF.empty:
        return ""
    names = find_players_in_text(query)
    if not names:
        # Also attempt token-based loose matches (helpful for one-name queries like "Haaland")
        tokens = set(re.findall(r"[a-zA-Z]+", query.lower()))
        for key in PLAYER_MAP.keys():
            last = key.split()[-1]
            if last in tokens:
                names.append(key)
        # Deduplicate again
        names = list(dict.fromkeys(names))
    if not names:
        return ""
    lines = []
    for nm in names[:6]:  # keep it short
        d = PLAYER_MAP.get(nm)
        if d:
            lines.append(_format_player_row(d))
    if not lines:
        return ""
    return "Player stats context:\n" + "\n".join(lines)

# --------------- FastAPI setup -----------------------------------
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="Soccer Pundit Bot")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

class ChatTurn(BaseModel):
    role: str  # "user" | "assistant" | "system"
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatTurn]
    mode: str = "pundit"        # "pundit" | "banter" | "compare" | "stats"
    hot_takes: bool = False
    max_tokens: int = 500

@app.on_event("startup")
def _startup():
    ok = _safe_load_players("players.csv")
    print(f"[startup] players.csv loaded: {ok}; rows={len(PLAYERS_DF)}")

@app.get("/health")
def health():
    return {
        "ok": True,
        "players_loaded": not PLAYERS_DF.empty,
        "rows": int(len(PLAYERS_DF)) if not PLAYERS_DF.empty else 0
    }

@app.get("/players")
def list_players(limit: int = 50):
    if PLAYERS_DF.empty:
        return {"players": []}
    return {"players": PLAYERS_DF.head(limit).to_dict(orient="records")}

@app.post("/chat")
def chat(req: ChatRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(500, "Missing OPENAI_API_KEY")

    user_query = req.messages[-1].content if req.messages else ""
    kb_hits = retrieve(user_query, KB, top_k=6)
    player_context = build_player_context(user_query)

    mode_instructions = {
        "pundit": "Be objective, balanced, and tactical.",
        "banter": "Add mild, friendly banter. Keep it respectful.",
        "compare": "Compare players/teams with role fit, outputs, system, and tactical context.",
        "stats": "Lean on evergreen rules and explain how stats like xG, PPDA, progressive passes matter."
    }.get(req.mode, "Be objective, balanced, and tactical.")

    spice = " Offer one bold but well-reasoned hot take at the end." if req.hot_takes else ""

    system = {"role": "system", "content": PUNDIT_SYSTEM_PROMPT + f"\nMode: {mode_instructions}{spice}"}

    kb_context = {"role": "system", "content": "Relevant evergreen context:\n" + "\n".join(kb_hits) if kb_hits else "No extra KB context."}

    if player_context:
        kb_context["content"] += "\n\n" + player_context

    messages = [system, kb_context] + [m.model_dump() for m in req.messages]

    try:
        resp = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=messages,
            temperature=0.7,
            max_tokens=req.max_tokens
        )
        answer = resp.choices[0].message.content
        return {
            "answer": answer,
            "kb_used": kb_hits,
            "players_context_added": bool(player_context)
        }
    except Exception as e:
        raise HTTPException(500, f"LLM error: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "7860")))

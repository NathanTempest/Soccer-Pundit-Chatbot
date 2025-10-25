# server.py
import os, re
from typing import List, Dict
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# ---------------- Evergreen KB ----------------
KB = """
# Competitions (evergreen overview)
- Premier League: 20 teams, 38 matches; 3 pts win / 1 draw; tiebreakers: GD then goals scored.
- La Liga: 20 teams; head-to-head used before goal difference in many seasons.
- UEFA Champions League: domestic qualification, group stage, knockouts, one-match final.

# Roles & positions
- 4-3-3: wingers give width; #6 anchors; fullbacks overlap or invert.
- 4-2-3-1: double pivot stability; #10 links midfield to striker.
- Pressing: high/mid/low blocks; rest defense prevents counters.
- xG: chance quality metric; separates process from finishing variance.

# Tactical talking points
- Build-up: CBs split, #6 drops; inverted FBs overload midfield.
- Transitions: counter-press “5s rule”; rest defense (2 CBs + DM).
- Set pieces: outswinger vs inswinger; zonal vs man-marking.

# Common pundit query patterns
- Compare players: role, outputs (G/A), system fit.
- Team struggles: spacing, pressing triggers, rest defense, xG delta.
- Predictions: probabilities + swing factors (injuries, fatigue, schedule).
"""

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

PUNDIT_SYSTEM_PROMPT = """
You are a charismatic, neutral football TV pundit.
Domains: Premier League, La Liga, UEFA Champions League.
Tone: confident, analytical, concise (3–6 tight paragraphs or bullets).
Use concrete concepts (4-3-3, #6/#10, pressing triggers, rest defense, xG).
Separate facts from opinions. For predictions, give probability ranges + swing factors.
If asked for real-time tables/fixtures, note they may have changed.
Keep banter friendly and respectful.
"""

# ---------------- Players CSV helpers ----------------
PLAYERS_DF = pd.DataFrame()
PLAYER_MAP: Dict[str, Dict] = {}
PLAYER_NAMES_LOWER: List[str] = []

def _safe_load_players(path: str = "players.csv"):
    global PLAYERS_DF, PLAYER_MAP, PLAYER_NAMES_LOWER
    try:
        df = pd.read_csv(path)
        for col in ["Goals", "Assists", "PassingAccuracy", "KeyPassesPer90"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        PLAYERS_DF = df.fillna("")
        PLAYER_MAP = {str(r["Name"]).strip().lower(): r.to_dict() for _, r in PLAYERS_DF.iterrows()}
        PLAYER_NAMES_LOWER = list(PLAYER_MAP.keys())
        return True
    except Exception:
        PLAYERS_DF = pd.DataFrame()
        PLAYER_MAP = {}
        PLAYER_NAMES_LOWER = []
        return False

def _fmt_player(d: Dict) -> str:
    return (
        f"{d.get('Name','')} ({d.get('Club','')}, {d.get('League','')}) — {d.get('Position','')} | "
        f"G:{d.get('Goals','')} A:{d.get('Assists','')} Pass%:{d.get('PassingAccuracy','')} "
        f"KP/90:{d.get('KeyPassesPer90','')} | Note: {d.get('StyleNotes','')}"
    )

def _find_players_in_text(text: str) -> List[str]:
    t = " " + text.lower() + " "
    names = []
    for nm in PLAYER_NAMES_LOWER:
        if f" {nm} " in t or t.strip().startswith(nm) or t.strip().endswith(nm):
            names.append(nm)
    # also try last-name loose matches
    tokens = set(re.findall(r"[a-zA-Z]+", text.lower()))
    for nm in PLAYER_NAMES_LOWER:
        last = nm.split()[-1]
        if last in tokens:
            names.append(nm)
    # dedupe in order
    seen, out = set(), []
    for n in names:
        if n not in seen:
            out.append(n); seen.add(n)
    return out[:6]

def build_player_context(query: str) -> str:
    if PLAYERS_DF.empty:
        return ""
    names = _find_players_in_text(query)
    if not names:
        return ""
    lines = []
    for nm in names:
        d = PLAYER_MAP.get(nm)
        if d:
            lines.append(_fmt_player(d))
    return "Player stats context:\n" + "\n".join(lines) if lines else ""

# ---------------- FastAPI app ----------------
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Use lifespan instead of deprecated on_event
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    _safe_load_players("players.csv")
    yield

app = FastAPI(title="Soccer Pundit Bot", lifespan=lifespan)

# CORS: allow ONLY your GitHub Pages origins in production
FRONTEND_ORIGINS = [
    "https://nathantempest.github.io",
    "https://nathantempest.github.io/Soccer-Pundit-Chatbot"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS if os.getenv("ENV", "prod") == "prod" else ["*"],
    allow_credentials=True,
    allow_methods=["POST","GET","OPTIONS"],
    allow_headers=["*"],
)

class ChatTurn(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatTurn]
    mode: str = "pundit"        # "pundit" | "banter" | "compare" | "stats"
    hot_takes: bool = False
    max_tokens: int = 500

# Health endpoints (Render default is /healthz)
@app.get("/health")
def health():
    return {"ok": True, "players_loaded": not PLAYERS_DF.empty, "rows": int(len(PLAYERS_DF)) if not PLAYERS_DF.empty else 0}

@app.get("/healthz")
def healthz():
    return {"ok": True}

# Optional: serve index.html from backend too (not required if using GitHub Pages)
@app.get("/", response_class=HTMLResponse)
def root():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return HTMLResponse("<h3>Soccer Pundit API is running</h3>", status_code=200)

@app.get("/players")
def list_players(limit: int = 50):
    if PLAYERS_DF.empty:
        return {"players": []}
    return {"players": PLAYERS_DF.head(limit).to_dict(orient="records")}

@app.get("/chat")
def chat_get(q: str = Query(..., description="Your question"),
             mode: str = "pundit", hot: bool = False, max_tokens: int = 400):
    # Convenience GET for quick tests in a browser
    user_msg = {"role": "user", "content": q}
    return _chat_core([user_msg], mode, hot, max_tokens)

@app.post("/chat")
def chat(req: ChatRequest):
    if not req.messages:
        raise HTTPException(400, "messages required")
    return _chat_core([m.model_dump() for m in req.messages], req.mode, req.hot_takes, req.max_tokens)

def _chat_core(messages: List[Dict], mode: str, hot: bool, max_tokens: int):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(500, "Missing OPENAI_API_KEY")

    user_query = messages[-1]["content"]
    kb_hits = retrieve(user_query, KB, top_k=6)
    player_context = build_player_context(user_query)

    mode_instructions = {
        "pundit": "Be objective, balanced, and tactical.",
        "banter": "Add mild, friendly banter. Keep it respectful.",
        "compare": "Compare players/teams with role fit, outputs, system, and tactical context.",
        "stats": "Lean on evergreen rules and explain how stats like xG, PPDA, progressive passes matter."
    }.get(mode, "Be objective, balanced, and tactical.")

    spice = " Offer one bold but well-reasoned hot take at the end." if hot else ""

    system = {"role": "system", "content": PUNDIT_SYSTEM_PROMPT + f"\nMode: {mode_instructions}{spice}"}
    kb_context = {"role": "system", "content": "Relevant evergreen context:\n" + "\n".join(kb_hits) if kb_hits else "No extra KB context."}
    if player_context:
        kb_context["content"] += "\n\n" + player_context

    try:
        resp = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[system, kb_context] + messages,
            temperature=0.7,
            max_tokens=max_tokens
        )
        answer = resp.choices[0].message.content
        return {
            "answer": answer,
            "kb_used": kb_hits,
            "players_context_added": bool(player_context)
        }
    except Exception as e:
        raise HTTPException(500, f"LLM error: {e}")

# Note: On Render you’ll start with gunicorn; this __main__ is for local dev.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "7860")))

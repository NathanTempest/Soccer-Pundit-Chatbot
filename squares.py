import random

# Players
players = [
    "Cbum", "Vulli", "Nathan", "Ravi anna", "Anil anna",
    "Harsha", "Netha", "Mujju", "Tiger", "Rahul"
]

BOARD_SIZE = 10
OUTPUT_FILE = "results.txt"

# Create hidden board
board = [
    [(random.randint(0, 9), random.randint(0, 9)) for _ in range(BOARD_SIZE)]
    for _ in range(BOARD_SIZE)
]

taken_squares = set()
assignments = {}

print("\n🎯 Welcome to the 10x10 Squares Game!")
print("Pick a square by entering: row column (both between 0 and 9)")
print("Example: 3 7\n")

# Interactive selection
for player in players:
    while True:
        try:
            choice = input(f"{player}, choose your square (row col): ").strip()
            row, col = map(int, choice.split())

            if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                print("❌ Row and column must be between 0 and 9.")
                continue

            if (row, col) in taken_squares:
                print("❌ That square is already taken. Choose another.")
                continue

            taken_squares.add((row, col))
            assignments[player] = (row, col)
            print(f"✅ {player} locked in square ({row}, {col})\n")
            break

        except ValueError:
            print("❌ Invalid input. Enter two numbers like: 4 6")

# Reveal + write results
with open(OUTPUT_FILE, "w") as file:
    file.write("🎉 FINAL RESULTS — 10x10 Squares Game\n\n")

    print("\n🎉 FINAL RESULTS:\n")
    for player, (row, col) in assignments.items():
        value = board[row][col]
        result_line = (
            f"{player} → Square ({row}, {col}) → Value {value}\n"
        )

        print(result_line.strip())
        file.write(result_line)

print(f"\n📁 Results saved to '{OUTPUT_FILE}'")
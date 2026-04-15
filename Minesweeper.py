import random

size = 5
mines = 5

# Create board
board = [["-" for _ in range(size)] for _ in range(size)]
mine_positions = set()

# Place mines
while len(mine_positions) < mines:
    r = random.randint(0, size - 1)
    c = random.randint(0, size - 1)
    mine_positions.add((r, c))

def count_mines(r, c):
    count = 0
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if (i, j) in mine_positions:
                count += 1
    return count

def print_board():
    print("\nBoard:")
    for row in board:
        print(" ".join(row))

# Game loop
while True:
    print_board()

    try:
        r = int(input("Enter row: "))
        c = int(input("Enter column: "))
    except ValueError:
        print("⚠️ Enter valid numbers!")
        continue

    if r < 0 or r >= size or c < 0 or c >= size:
        print("⚠️ Out of bounds!")
        continue

    if (r, c) in mine_positions:
        print("💥 Boom! You hit a mine. Game Over!")
        break
    else:
        board[r][c] = str(count_mines(r, c))

    # Win check
    safe_cells = size * size - mines
    opened = sum(cell != "-" for row in board for cell in row)

    if opened == safe_cells:
        print_board()
        print("🎉 You cleared the board! You win!")
        break

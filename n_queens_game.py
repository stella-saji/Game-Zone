def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(n):
        if board[i][col]:
            return False

    # Check row
    for j in range(n):
        if board[row][j]:
            return False

    # Check diagonals
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                if abs(i - row) == abs(j - col):
                    return False

    return True


def play_n_queens():
    print("♛ Welcome to the N-Queens Game ♛")

    while True:
        try:
            n = int(input("Enter number of queens (N): "))
            if n < 1:
                print("Enter a number >= 1")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    board = [[0 for _ in range(n)] for _ in range(n)]
    queens_placed = 0

    while queens_placed < n:
        print_board(board)

        try:
            row = int(input(f"Enter row (0 to {n-1}): "))
            col = int(input(f"Enter column (0 to {n-1}): "))

            if row < 0 or row >= n or col < 0 or col >= n:
                print("⚠️ Invalid position! Try again.")
                continue

            if board[row][col] == 1:
                print("⚠️ A queen is already there!")
                continue

            if is_safe(board, row, col, n):
                board[row][col] = 1
                queens_placed += 1
                print("✅ Queen placed!")
            else:
                print("❌ Invalid move! Queens attack each other.")

        except ValueError:
            print("⚠️ Please enter valid numbers.")

    print_board(board)
    print("🎉 Congratulations! You placed all queens correctly!")


# Run the game
play_n_queens()

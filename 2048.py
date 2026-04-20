import random

size = 4

def create_board():
    board = [[0]*size for _ in range(size)]
    add_tile(board)
    add_tile(board)
    return board

def add_tile(board):
    empty = [(i, j) for i in range(size) for j in range(size) if board[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 2

def print_board(board):
    print("\n")
    for row in board:
        print(" ".join(str(num).rjust(4) if num != 0 else "   ." for num in row))
    print()

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (size - len(new_row))
    return new_row

def merge(row):
    for i in range(size-1):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    new_board = []
    for row in board:
        row = compress(row)
        row = merge(row)
        row = compress(row)
        new_board.append(row)
    return new_board

def rotate(board):
    return list(zip(*board[::-1]))

def move(board, direction):
    for _ in range(direction):
        board = rotate(board)
    board = move_left(board)
    for _ in range((4 - direction) % 4):
        board = rotate(board)
    return [list(row) for row in board]

def game_over(board):
    for row in board:
        if 0 in row:
            return False
    for i in range(size):
        for j in range(size-1):
            if board[i][j] == board[i][j+1] or board[j][i] == board[j+1][i]:
                return False
    return True

def play():
    board = create_board()

    while True:
        print_board(board)
        move_input = input("Move (w/a/s/d): ").lower()

        if move_input == 'a':
            new_board = move(board, 0)
        elif move_input == 'w':
            new_board = move(board, 1)
        elif move_input == 'd':
            new_board = move(board, 2)
        elif move_input == 's':
            new_board = move(board, 3)
        else:
            print("Invalid input!")
            continue

        if new_board != board:
            board = new_board
            add_tile(board)

        if game_over(board):
            print_board(board)
            print("💀 Game Over!")
            break

play()

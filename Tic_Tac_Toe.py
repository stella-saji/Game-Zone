board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_positions)

player = "X"

for turn in range(9):
    print_board()
    move = int(input(f"Player {player}, choose position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = player
        if check_winner(player):
            print_board()
            print(f"🎉 Player {player} wins!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("⚠️ Spot already taken, try again!")
        continue
else:
    print_board()
    print("🤝 It's a draw!")

line_one = list(map(int, input().split()))
line_two = list(map(int, input().split()))
line_three = list(map(int, input().split()))

board = [line_one, line_two, line_three]
winner = 0

if winner == 0:
    for row in board:
        if row.count(1) == 3:
            winner = 1
            break
        elif row.count(2) == 3:
            winner = 2
            break

if winner == 0:
    for c in range(3):
        col = [board[0][c], board[1][c], board[2][c]]
        if col.count(1) == 3:
            winner = 1
            break
        elif col.count(2) == 3:
            winner = 2
            break

if winner == 0:
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]

    if diag1.count(1) == 3 or diag2.count(1) == 3:
        winner = 1
    elif diag1.count(2) == 3 or diag2.count(2) == 3:
        winner = 2

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
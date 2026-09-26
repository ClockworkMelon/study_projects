board_size = int(input())
board = [[x for x in input()] for _ in range(board_size)]
knights = []

for row in range(board_size):
    for col in range(board_size):
        if board[row][col] == "K":
            knights.append([row, col])

MOVES = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
knights_removed = 0

while True:
    max_hits = 0
    max_knight = [0, 0]

    for knight_row, knight_col in knights:
        hits = 0
        for d_row, d_col in MOVES:
            new_row, new_col = knight_row + d_row, knight_col + d_col
            if 0 <= new_row < board_size and 0 <= new_col < board_size and board[new_row][new_col] == "K":
                hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [knight_row, knight_col]

    if max_hits == 0:
        break

    knights.remove(max_knight)
    board[max_knight[0]][max_knight[1]] = 0
    knights_removed += 1

print(knights_removed)
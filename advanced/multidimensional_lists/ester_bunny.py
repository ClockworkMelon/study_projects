size = int(input())

field = []
bunny_row = bunny_col = 0

for r in range(size):
    row = input().split()
    if "B" in row:
        bunny_row, bunny_col = r, row.index("B")
    field.append(row)

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right":(0, 1)
}

max_eggs_collected = -float("inf")
best_moves = []
direction = ""

for key, (dr_row, dr_col) in DIRECTIONS.items():
    moves = []
    eggs_collected = 0
    new_row, new_col = bunny_row + dr_row, bunny_col + dr_col
    while 0 <= new_row < size and 0 <= new_col < size:

        if field[new_row][new_col] == "X":
            break

        eggs_collected += int(field[new_row][new_col])
        moves.append([new_row, new_col])

        new_row += dr_row
        new_col += dr_col

    if eggs_collected > max_eggs_collected and moves:
        max_eggs_collected = eggs_collected
        best_moves = moves
        direction = key

print(direction)
print(*best_moves, sep="\n")
print(max_eggs_collected)

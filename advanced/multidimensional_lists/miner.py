rows = int(input())
commands = [x for x in input().split()][::-1]
matrix = [[x for x in input().split()] for _ in range(rows)]

miner = 's'
coal = 'c'
route_end = "e"
field_position = "*"

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right":(0, 1)
}

miner_row, miner_col = 0, 0
exit_row, exit_col = 0, 0
available_coal = 0

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == miner:
            miner_row, miner_col = row, col
        elif matrix[row][col] == coal:
            available_coal += 1
        elif matrix[row][col] == route_end:
            exit_row, exit_col = row, col

game_over = False
coal_collected = 0

while len(commands) > 0 and available_coal > 0:
    command = commands.pop()
    dir_row, dir_col = DIRECTIONS[command]

    if not 0 <= (miner_row + dir_row) < rows or not 0 <= (miner_col + dir_col) < rows:
        continue
    else:
        miner_row, miner_col = miner_row + dir_row, miner_col + dir_col
        matrix[miner_row - dir_row][miner_col - dir_col] = "*"

        if matrix[miner_row][miner_col] == "c":
            coal_collected += 1
            available_coal -= 1
            matrix[miner_row][miner_col] = "*"
        elif matrix[miner_row][miner_col] == "e":
            game_over = True
            break

if available_coal == 0 and not game_over:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif not commands and not game_over:
    print(f"{available_coal} pieces of coal left. ({miner_row}, {miner_col})")
elif game_over:
    print(f'Game over! ({exit_row}, {exit_col})')


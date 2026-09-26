rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]

coordinates_line = input().split()
coordinates = []

for element in coordinates_line:
    row, col = element.split(",")
    coordinates.append((int(row), int(col)))

for bomb_row, bomb_col in coordinates:
    bomb_value = matrix[bomb_row][bomb_col]
    if bomb_value <= 0:
        continue

    matrix[bomb_row][bomb_col] = 0

    for row in range(bomb_row - 1, bomb_row + 2):
        for col in range(bomb_col - 1, bomb_col + 2):
            if 0 <= row < rows and 0 <= col < rows:
                if matrix[row][col] > 0:
                    matrix[row][col] -= bomb_value

alive_cells = 0
alive_sum = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            alive_sum += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")

for row in matrix:
    print(*row)
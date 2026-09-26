matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

def valid_coordinates(r, c):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)

while True:
    command = input().split()
    if command[0] == "END":
        break

    action = command[0]
    act_row = int(command[1])
    act_col = int(command[2])
    value = int(command[3])

    if not valid_coordinates(act_row, act_col):
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[act_row][act_col] += value
    elif action == "Subtract":
        matrix[act_row][act_col] -= value

for row in matrix:
    print(*row)
def valid_commands(comm: list):
    return comm[0] == "swap" and len(comm) == 5 and any(int(x) >= 0 for x in comm[1:])

def valid_coordinates(r1, c1, r2, c2):
    return r1 <= len(matrix) and r2 <= len(matrix) and c1 <= len(matrix[r1]) and c2 <= len(matrix[r2])

rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]

while True:
    line = input()

    if line == "END":
        break

    commands = line.split()
    action = commands[0]

    if not valid_commands(commands):
        print("Invalid input!")
        continue
    else:
        row1, col1, row2, col2 = [int(x) for x in commands[1:]]
        if valid_coordinates(row1, col1, row2, col2):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print("Invalid input!")


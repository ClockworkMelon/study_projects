rows, columns = input().split(", ")

matrix = []

for _ in range(int(rows)):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for column in range(int(columns)):
    column_sum = 0
    for row in range(int(rows)):
        column_sum += matrix[row][column]
    print(column_sum)

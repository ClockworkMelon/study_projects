rows, cols = [int(x) for x in input().split()]

start = ord("a")
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        middle = start + col
        matrix[row].append(chr(start) + chr(middle) + chr(start))

    start += 1

[print(*row) for row in matrix]
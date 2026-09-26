rows, columns = input().split(", ")
matrix = []

for _ in range(int(rows)):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

matrix_sum = 0
for row, elements in enumerate(matrix):
    matrix_sum += sum(elements)

print(matrix_sum)
print(matrix)
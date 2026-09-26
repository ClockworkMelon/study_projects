rows = int(input())

matrix = []

for _ in range(rows):
     row = [int(x) for x in input().split(", ")]
     matrix.append(row)

flattened_matrix = []
for row, element in enumerate(matrix):
    for num in element:
        flattened_matrix.append(num)

print(flattened_matrix)
rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

found_matrix = []
sum_of_matrix = -float("inf")

for row in range(rows -1):
    for col in range(cols -1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > sum_of_matrix:
            sum_of_matrix = current_sum
            found_matrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]


[print(*row) for row in found_matrix]
print(sum_of_matrix)
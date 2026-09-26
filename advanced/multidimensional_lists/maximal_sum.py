rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

found_matrix = []
largest_sum = -float("inf")

for row in range(rows - 2):
    for col in range(cols - 2):
        curr_row_one = list(matrix[row][col:col + 3])
        curr_row_two = list(matrix[row + 1][col:col + 3])
        curr_row_tree = list(matrix[row + 2][col:col + 3])
        current_sum = sum(curr_row_one) + sum(curr_row_two) + sum(curr_row_tree)
        if current_sum > largest_sum:
            largest_sum = current_sum
            found_matrix = [curr_row_one, curr_row_two, curr_row_tree]

print(f'Sum = {largest_sum}')
[print(*row) for row in found_matrix]
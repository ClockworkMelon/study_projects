matrix = [[int(x) for x in input().split()] for row in range(int(input()))]

sum_diagonal = 0
current_row = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if current_row == row:
            sum_diagonal += matrix[row][current_row]
            current_row += 1

print(sum_diagonal)


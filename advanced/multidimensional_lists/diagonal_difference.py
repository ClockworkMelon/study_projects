matrix = [[int(x) for x in input().split()] for row in range(int(input()))]

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][-1 - i] for i in range(len(matrix))]

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)
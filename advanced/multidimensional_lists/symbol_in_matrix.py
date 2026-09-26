matrix = [[x for x in input()] for row in range(int(input()))]
searched_symbol = input()

found_row, found_col = 0, 0
symbol_found = False

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_symbol:
            found_row, found_col = row, col
            symbol_found = True
            break
            
    if symbol_found:
        break

if symbol_found:
    print(f"({found_row}, {found_col})")
else:
    print(f'{searched_symbol} does not occur in the matrix')
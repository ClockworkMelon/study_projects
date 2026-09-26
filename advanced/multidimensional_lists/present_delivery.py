presents_count = int(input())
size = int(input())
neighborhood = []
santa_r = santa_c = 0
nice_kids = 0
nice_kids_left = 0

for r in range(size):
    row = input().split()
    neighborhood.append(row)
    if "S" in row:
        santa_r, santa_c = r, row.index("S")
        neighborhood[santa_r][santa_c] = "-"
    nice_kids_left += row.count("V")

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right":(0, 1)
}

while presents_count > 0:
    dr = input()
    if dr == "Christmas morning":
        break

    dr_row, dr_col = DIRECTIONS[dr]
    santa_r, santa_c = santa_r + dr_row, santa_c + dr_col

    if 0 <= santa_r < size and 0 <= santa_c < size:
        santa_r_old, santa_c_old = santa_r - dr_row, santa_c - dr_col
        if neighborhood[santa_r][santa_c] == "V":
            presents_count -= 1
            nice_kids += 1
        elif neighborhood[santa_r][santa_c] == "C":
            for c_row, c_col in DIRECTIONS.values():
                if presents_count == 0:
                    break
                target_row, target_col = santa_r + c_row, santa_c + c_col
                if 0 <= target_row < size and 0 <= target_col < size and neighborhood[target_row][target_col] in "VX":
                    presents_count -= 1
                    if neighborhood[target_row][target_col] == "V":
                        nice_kids += 1
                    neighborhood[target_row][target_col] = "-"

        neighborhood[santa_r_old][santa_c_old] = "-"
        neighborhood[santa_r][santa_c] = "S"

nice_kids_left -= nice_kids

if presents_count == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if nice_kids_left > 0:
    print(f"No presents for {nice_kids_left} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
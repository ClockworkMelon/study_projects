matrix = [input().split() for _ in range(5)]

player_r = player_c = 0
targets_shot = []
targets_count = 0
for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            player_r, player_c = row, col
        elif matrix[row][col] == "x":
            targets_count += 1

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right":(0, 1)
}



for _ in range(int(input())):
    act, dr, *distance = input().split()
    dr_row, dr_col = DIRECTIONS[dr]

    if act == "shoot":
        row = player_r + dr_row
        col = player_c + dr_col
        while 0 <= row < 5 and 0 <= col < 5:
            if matrix[row][col] == "x":
                targets_count -= 1
                matrix[row][col] = "."
                targets_shot.append([row, col])
                break
            row += dr_row
            col += dr_col

        if targets_count == 0:
            print(f"Training completed! All {len(targets_shot)} targets hit.")
            break

    elif act == "move":
        distance_count = int(distance[0])
        row = player_r + dr_row * distance_count
        col = player_c + dr_col * distance_count

        if 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == ".":
            matrix[player_r][player_c] = "."
            matrix[row][col] = "A"
            player_r, player_c = row, col

if targets_count > 0:
    print(f"Training not completed! {targets_count} targets left.")

for row in targets_shot:
    print(row)
rows = int(input())
row = []

for i in range(rows):
    row.append(list(input()))

kr = kc = None
for i in range(rows):
    for j in range(len(row[i])):
        if row[i][j] == "k":
            kr, kc = i, j
            break
    if kr is not None:
        break

moves = 0

while True:
    if kr == 0 or kr == rows - 1 or kc == 0 or kc == len(row[kr]) - 1:
        print(f"Kate got out in {moves} moves")
        break

    if kr + 1 < rows and row[kr + 1][kc] == " ":
        kr += 1
        moves += 1
        continue

    moved = False
    if kc - 1 >= 0 and row[kr][kc - 1] == " ":
        kc -= 1
        moves += 1
        moved = True
    elif kc + 1 < len(row[kr]) and row[kr][kc + 1] == " ":
        kc += 1
        moves += 1
        moved = True

    if moved:
        continue

    print("Kate cannot get out")
    break

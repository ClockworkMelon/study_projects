size = int(input())

territory = [[x for x in input().split()] for _ in range(size)]

alice_r = alice_c = 0

for row in range(size):
    for col in range(size):
        if territory[row][col] == "A":
            alice_r, alice_c = row, col

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right":(0, 1)
}

teabags = 0
territory[alice_r][alice_c] = "*"
alice_left = False

while teabags < 10:
    dr = input()
    dr_row, dr_col = DIRECTIONS[dr]

    alice_r, alice_c = alice_r + dr_row, alice_c + dr_col

    if not (0 <= alice_r < size and 0 <= alice_c < size):
        alice_left = True
        break

    if territory[alice_r][alice_c] == "R":
        territory[alice_r][alice_c] = "*"
        alice_left = True
        break

    if territory[alice_r][alice_c].isdigit():
        teabags += int(territory[alice_r][alice_c])

    territory[alice_r][alice_c] = "*"

if teabags >= 10:
    print("She did it! She went to the party.")

if alice_left:
    print("Alice didn't make it to the tea party.")

[print(*row, sep=" ") for row in territory]


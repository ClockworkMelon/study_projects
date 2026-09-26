rows, cols = map(int, input().split())
lair = []
pr = pc = 0

for r in range(rows):
    line = input()
    lair.append(list(line))
    if "P" in line:
        pr, pc = r, line.index("P")

commands = input()
moves = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

def spread(l):
    new = [row[:] for row in l]
    for r in range(rows):
        for c in range(cols):
            if l[r][c] == "B":
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        new[nr][nc] = "B"
    return new

for cmd in commands:
    dr, dc = moves[cmd]
    nr, nc = pr + dr, pc + dc
    escaped = False
    dead = False
    last_r, last_c = pr, pc

    if not (0 <= nr < rows and 0 <= nc < cols):
        escaped = True
        lair[pr][pc] = "."
    else:
        if lair[nr][nc] == "B":
            dead = True
            lair[pr][pc] = "."
            pr, pc = nr, nc
        else:
            lair[pr][pc] = "."
            pr, pc = nr, nc
            lair[pr][pc] = "P"

    lair = spread(lair)

    if escaped:
        for row in lair:
            print("".join(row))
        print(f"won: {last_r} {last_c}")
        break

    if lair[pr][pc] == "B":
        dead = True

    if dead:
        for row in lair:
            print("".join(row))
        print(f"dead: {pr} {pc}")
        break

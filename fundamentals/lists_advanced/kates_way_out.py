# Kate is stuck in a maze. You should help her to find her way out.
# On the first line, you will be given how many rows there are in the maze. On the following n lines,
# you will be given the maze itself. Here is a legend for the maze:
# •	"#" - means a wall; Kate cannot go through there
# •	" " - means empty space; Kate can go through there
# •	"k" - the initial position of Kate; start looking for a way out from there
# There are two options: Kate either gets out or not:
# •	If Kate can get out, print the following:
# "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
# •	Otherwise, print: "Kate cannot get out".

rows = int(input())
row = []

for i in range(rows):
    row.append(list(map(str, input())))

paths = []
start = []
blocked_row = False

for i in range(1, rows):
    path = []
    blocked = 0
    more_paths_count = 0

    for y in range(len(row[i])):
        if row[i][y] != "#":
            if row[i][y].isspace():
                path.append(i)
                path.append(y)
            else:
                start.append(i)
                start.append(y)
        else:
            blocked += 1

            if blocked == len(row[i]):
                blocked_row = True
                break

    blocked = 0

    if blocked_row:
        break

    paths.append(path)

exit_position = []
add_moves = 0

if blocked_row:
    print(f'Kate cannot get out')
    exit()

for k in range(len(paths)):
    if len(paths[k]) > 2:
        add_moves += (len(paths[k]) // 2) - 1

for k in range(len(paths)):
    lenght = len(paths[k])
    if lenght > 2:
        counter = 1
        for x in range(lenght - 2):
            if counter == 1:
                exit_position.append(paths[k][x + 1])
            counter += 2
        lenght -= 2
    else:
        if lenght == 2:
            exit_position.append(paths[k][1])

moves = len(exit_position) + add_moves + 1

print(f'Kate got out in {moves} moves')

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

def labyrinth(rows):
    """
    :param rows: RECEIVES STRING
    :return: LIST OF STRINGS - We'll use as a matrix
    :example:   ['#######',
                 '###  K#',
                 '#######',
                 '##### #',
                 '## ####']
    """
    maze_rows_accumulator = []
    for i in range(rows):
        row_count = input()
        maze_rows_accumulator.append(row_count)
    return maze_rows_accumulator

def kate_index(maze_):
    idx_col = 0
    idx_row = 0
    kate = []
    found_kate = False
    for x in maze_:
        idx_row = maze_.index(x)
        for i in x:
            if i == 'k' or i == 'K':
                found_kate = True
                idx_col = x.index(i)
                break
        if found_kate:
            kate.append(idx_row)
            kate.append(idx_col)
            break

    return kate

def is_there_exit(maze_):
    way_out_ = True
    blockades = 0
    for x in maze_:
        if " " not in x:
            blockades += 1
            if blockades == 2:
                way_out_ = False
                break
    return way_out_

maze = labyrinth(int(input()))
kate_position = kate_index(maze)

def exit_moves(maze_):
    kates_row = kate_position[0]
    moves = 1
    kates_row_spaces = 0
    furthest_space_from_kate = 0
    for x in range(kates_row, len(maze_)):
        for i in range(len(maze_[x])):
            if maze_[x][i] == " " and 'k' in maze_[x]:
                moves += 1
                furthest_space_from_kate = kate_position[1] - i + 1
                if furthest_space_from_kate < kates_row_spaces:
                    kates_row_spaces = furthest_space_from_kate
            elif maze_[x][i] == " " and 'k' not in maze_[x]:
                if i == furthest_space_from_kate and maze_[x][i] == " ":
                    moves += 1
                elif i == furthest_space_from_kate and maze_[x + 1][i] == '#':
                    if maze_[x][i + 1] == " ":
                        moves + 1


    return moves



way_out = is_there_exit(maze)

if way_out:
    exits = exit_moves(maze)
    print(f'Kate got out in {exits} moves')
else:
    print(f'Kate cannot get out')





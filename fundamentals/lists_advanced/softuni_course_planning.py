courses = list(map(str, input().split(', ')))

while True:
    command = input().split(':')

    if command[0] == 'course start':
        break
    else:
        com_one = command[0]
        com_two = command[1]
        if len(command) == 3:
            com_tree = command[2]

    if com_one == 'Add' and com_two not in courses:
        courses.append(com_two)
    elif com_one == 'Insert' and com_two not in courses:
        courses.insert(int(com_tree), com_two)
    elif com_one == 'Remove' and com_two in courses:
        courses.remove(com_two)
    elif com_one == 'Swap' and (com_two in courses and com_tree in courses):
        if f"{com_tree}-Exercise" in courses:
            com_two_index = courses.index(com_two)
            ex_index = courses.index(f"{com_tree}-Exercise")
            com_tree_index = courses.index(com_tree)
            courses[com_two_index], courses[com_tree_index] = \
            (
                courses[com_tree_index],
                courses[com_two_index]
            )
            exer = courses.pop(ex_index)
            courses.insert(com_two_index + 1, exer)
        else:
            com_two_index = courses.index(com_two)
            com_tree_index = courses.index(com_tree)
            courses[com_two_index], courses[com_tree_index] = courses[com_tree_index], courses[com_two_index]
    elif com_one == 'Exercise':
        if com_two in courses and f'{com_two}-Exercise' not in courses:
            course_index = courses.index(com_two)
            com = "-Exercise".join(com_two)
            courses.insert(course_index + 1, com)
        if com_two not in courses:
            com = f'{com_two}-Exercise'
            courses.append(com_two)
            courses.append(com)

for i in range(len(courses)):
    print(f'{i +1}.{courses[i]}')
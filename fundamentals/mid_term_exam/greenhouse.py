veggies = input().split(' & ')
commands = ['Plant', 'Transplant', 'Replace', 'Uproot']

while True:
    command = input().split()

    if command[0] == 'Collect!':
        break

    if command[0] == commands[0]:
        if command[1] not in veggies:
            veggies.insert(0, command[1])
    elif command[0] == commands[1]:
        if command[1] in veggies:
            transplanted_veggie = veggies.pop(veggies.index(command[1]))
            veggies.append(transplanted_veggie)
    elif command[0] == commands[2]:
        if int(command[1]) <= (len(veggies) - 1) and int(command[2]) <= (len(veggies) - 1):
            veggies[int(command[1])], veggies[int(command[2])] = veggies[int(command[2])], veggies[int(command[1])]
    elif command[0] == commands[3]:
        if command[1] in veggies:
            veggies.remove(command[1])

print(' | '.join(veggies))

wagons = int(input())
train = []

while True:
    command = input()

    if command == 'End':
        break

    if not len(train) == wagons:
        for x in range(wagons):
            train.append(0)

    command = list(command.split(' '))
    action_one = command[0]
    action_two = command[1]

    if len(command) == 3:
        action_three = command[2]

    if action_one == 'add':
        train[wagons - 1] += int(action_two)
    elif action_one == 'insert':
        train[int(action_two)] += int(action_three)
    elif action_one == 'leave':
        train[int(action_two)] -= int(action_three)

print(train)

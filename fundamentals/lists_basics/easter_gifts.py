gifts = input().split()
length = len(gifts)

while True:
    command = input()

    if command == "No Money":
        break

    command = command.split()

    action = command[0]

    if action == "OutOfStock":
        item = command[1]
        gifts = ["None" if x == item else x for x in gifts]

    elif action == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gift = command[1]
        gifts[-1] = gift

result = " ".join(x for x in gifts if x != "None")
print(result)
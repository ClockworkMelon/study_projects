card_dec = input().split(', ')
number = int(input())
commands = ['Add', 'Remove', 'Remove At', 'Insert']

for i in range(number):
    command = input().split(', ')

    if command[0] == commands[0]:
        if command[1] not in card_dec:
            card_dec.append(command[1])
            print(f"Card successfully added")
        else:
            print(f"Card is already in the deck")
    elif command[0] == commands[1]:
        if command[1] in card_dec:
            card_dec.remove(command[1])
            print(f"Card successfully removed")
        else:
            print(f"Card not found")
    elif command[0] == commands[2]:
        if (len(card_dec) - 1) >= int(command[1]) > 0:
            card_dec.remove(card_dec[int(command[1])])
            print(f"Card successfully removed")
        else:
            print(f"Index out of range")
    elif command[0] == commands[3]:
        if (len(card_dec) - 1) >= int(command[1]) > 0 and command[2] not in card_dec:
            card_dec.insert(int(command[1]), command[2])
            print(f"Card successfully added")
        elif (len(card_dec) - 1) >= int(command[1]) > 0 and command[2] in card_dec:
            print(f"Card is already added")
        elif int(command[1]) > (len(card_dec) - 1) or int(command[1]) < 0:
            print(f"Index out of range")

print(', '.join(card_dec))


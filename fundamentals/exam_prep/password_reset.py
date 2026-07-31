gibberish = input()
commands = input()
new_gibberish = ""

while commands != "Done":
    commands = commands.split()

    action = commands[0]

    if action == "TakeOdd":
        for index in range(len(gibberish)):
            if index % 2 == 1:
                 new_gibberish += gibberish[index]
        gibberish = new_gibberish
        new_gibberish = ''
        print(gibberish)
    elif action == "Cut":
        from_index = int(commands[1])
        length = int(commands[2])
        to_index = from_index + length
        substring = gibberish[from_index : to_index]
        gibberish = gibberish.replace(substring,'', 1)
        print(gibberish)
    elif action == "Substitute":
        old = commands[1]
        new = commands[2]
        if old in gibberish:
            gibberish = gibberish.replace(old, new)
            print(gibberish)
        else:
            print(f"Nothing to replace!")
    commands = input()

print(f'Your password is: {gibberish}')

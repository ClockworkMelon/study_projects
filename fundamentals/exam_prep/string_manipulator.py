gibberish = input()

commands = input()

while commands != "End":
    commands = commands.split()

    action = commands[0]

    if action == "Translate":
        old = commands[1]
        new = commands[2]
        if old in gibberish:
            gibberish = gibberish.replace(old, new)
        print(gibberish)

    elif action == "Includes":
        substring = commands[1]
        if substring in gibberish:
            print(True)
        else:
            print(False)
    elif action == "Start":
        substring = commands[1]
        if gibberish.startswith(substring):
            print(True)
        else:
            print(False)
    elif action == "Lowercase":
        gibberish = gibberish.lower()
        print(gibberish)
    elif action == "Remove":
        index = int(commands[1])
        end = int(commands[2])
        end_index = index + end
        substring = gibberish[index : end_index]
        gibberish = gibberish.replace(substring, "")
        print(gibberish)
    elif action == "FindIndex":
        char = commands[1]
        found_char = gibberish.rfind(char)
        print(found_char)
    commands = input()

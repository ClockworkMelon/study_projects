hidden_message = input()

command = input()

while command != "Reveal":

    commands = command.split(":|:")

    action = commands[0]

    if action == "InsertSpace":
        index = int(commands[1])
        hidden_message = hidden_message[:index] + " " + hidden_message[index:]
        print(hidden_message)
    elif action == "Reverse":
        substring = commands[1]
        if substring in hidden_message:
            new_substring = substring[::-1]
            hidden_message = hidden_message.replace(substring, new_substring, 1)
            print(hidden_message)
        else:
            print('error')
    elif action == "ChangeAll":
        old = commands[1]
        new = commands[2]
        hidden_message = hidden_message.replace(old, new)
        print(hidden_message)
    command = input()

print(f'You have a new text message: {hidden_message}')
import re
number_of_strings = int(input())

for cmd_str in range(number_of_strings):
    command_strings = input()
    pattern = r'!([A-Z]{1}[a-z]{2,})!:\[([a-zA-Z]{8,})\]'
    match = re.search(pattern, command_strings)
    list_of_numbers = []
    message = ""
    command = ""
    if not match:
        print(f'The message is invalid')
    else:
        message = match.group(2)
        command = match.group(1)

        for element in message:
            list_of_numbers.append(str(ord(element)))

        print(f'{command}: {" ".join(list_of_numbers)}')
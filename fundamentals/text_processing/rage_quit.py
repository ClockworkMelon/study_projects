rage_input = input()
rage_message = ""
current_letters = ''
repeats = ""

for index in range(len(rage_input)):
    if not rage_input[index].isdigit():
        current_letters += rage_input[index].upper()
    else:
        repeats += rage_input[index]
        if index + 1 < len(rage_input):
            if rage_input[index + 1].isdigit():
                repeats += rage_input[index + 1]
        rage_message += current_letters * int(repeats)
        current_letters = ""
        repeats = ""
print(f'Unique symbols used: {len(set(rage_message))}')
print(rage_message)
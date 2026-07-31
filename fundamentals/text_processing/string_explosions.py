string_line = input()
exploded_string = ""
strength = 0

for index in range(len(string_line)):

    if string_line[index] == ">":
        exploded_string += ">"
        strength += int(string_line[index + 1])

    elif strength > 0 and string_line[index] != ">":
        strength -= 1

    else:
        exploded_string += string_line[index]

print(f'{exploded_string}')
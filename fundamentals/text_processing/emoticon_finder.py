string_line = input()

for char in range(len(string_line) - 1):
    if string_line[char] == ":":
        print(f'{string_line[char]}{string_line[char + 1]}')
string_line = input()

for char in string_line:
    print(f'{chr(ord(char) + 3)}',end='')
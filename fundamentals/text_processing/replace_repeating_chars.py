string_line = input()
new_line = ''
for char in string_line:
    if not new_line or char != new_line[-1]:
        new_line += char

print(new_line)
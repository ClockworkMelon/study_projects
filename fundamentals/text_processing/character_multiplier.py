string_line_one, string_line_two = input().split()

total = 0

if len(string_line_one) > len(string_line_two):
    for char in range(len(string_line_two)):
        total += ord(string_line_one[char]) * ord((string_line_two[char]))

    for char in string_line_one[len(string_line_two):]:
        total += ord(char)
elif len(string_line_two) > len(string_line_one):
    for char in range(len(string_line_one)):
        total += ord(string_line_one[char]) * ord(string_line_two[char])

    for char in string_line_two[len(string_line_one):]:
        total += ord(char)
else:
    for char in range(len(string_line_one)):
        total += ord(string_line_one[char]) * ord(string_line_two[char])

print(total)

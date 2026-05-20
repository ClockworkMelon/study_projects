string_one = input().split(', ')
string_two = input().split(', ')
found_values = []

for x in range(len(string_one)):
    for y in string_two:
        if string_one[x] in y:
            found_values.append(string_one[x])
            break

print(found_values)
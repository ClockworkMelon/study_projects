first_string = input()
second_string = input()

for i in range(len(first_string)):
    left = second_string[:i + 1]
    right = first_string[i + 1:]
    new_string = left + right

    if second_string[i] != first_string[i]:
        print(new_string)
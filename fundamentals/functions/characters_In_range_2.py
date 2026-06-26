def chars(char_one, char_two):
    list_of_chars_in_between = []
    for i in range(ord(char_one) + 1, ord(char_two)):
        list_of_chars_in_between.append(chr(i))

    return " ".join(list_of_chars_in_between)

char_1 = input()
char_2 = input()

print(chars(char_1, char_2))


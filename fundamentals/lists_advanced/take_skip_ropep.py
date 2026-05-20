string = input()
num_list = []
char_list = []
skip_list = []
take_list = []
result_string = []

for i in string:
    if i.isdigit():
        num_list.append(int(i))
    else:
        char_list.append(i)

for i in range(len(num_list)):
    if i % 2 == 0:
        take_list.append(num_list[i])
    else:
        skip_list.append(num_list[i])

for i in range(len(take_list)):
    take = take_list[i]
    skip = skip_list[i]
    if take > 0 and skip == 0:
        result_string.append(''.join(char_list[0:take]))
        del char_list[0:take]
    elif take == 0 and skip > 0:
        del char_list[0:skip]
    elif take > 0 and skip > 0:
        result_string.append(''.join(char_list[0:take]))
        del char_list[0:take]
        del char_list[0:skip]

final = ''.join(result_string)

print(final)

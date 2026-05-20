string = list(map(int, input().split('.')))

if string[2] < 9:
    string[2] += 1
elif string[1] < 9:
    string[1] += 1
    string[2] = 0
else:
    string[0] += 1
    string[1] = 0
    string[2] = 0

print(f'{".".join(str(x) for x in string)}')



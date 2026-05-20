strings = input().split(' ')

for x in range(len(strings)):
    if len(strings[x]) % 2 == 0:
        print(strings[x])
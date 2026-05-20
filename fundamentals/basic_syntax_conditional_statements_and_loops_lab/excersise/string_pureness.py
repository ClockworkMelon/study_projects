strings = int(input())

for string in range(strings):
    line = input()

    if ',' in line or '_' in line or '.' in line:
        print(f'{line} is not pure!')
    else:
        print(f'{line} is pure.')


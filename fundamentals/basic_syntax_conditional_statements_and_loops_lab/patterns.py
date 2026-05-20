num = int(input())

for row in range(1, num + 1):
    for star in range(0, row):
        print(f'*', end='')
    print()

for row in range(num, 0, -1):
    for star in range(row - 1, 0, -1):
        print(f'*', end='')
    print()
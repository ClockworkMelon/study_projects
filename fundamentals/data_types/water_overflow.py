lines = int(input())
capacity = 0
for _ in range(1, lines + 1):
    littres = int(input())

    if capacity + littres <= 255:
        capacity += littres
    else:
        print(f'Insufficient capacity!')

print(f'{capacity}')


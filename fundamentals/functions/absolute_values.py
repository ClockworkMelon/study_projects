def absolute_values(abc):
    for x in range(len(abc)):
        if abc[x] < 0:
            abc[x] *= -1
    return abc


line = list(map(float, input().split(' ')))

print(f'{absolute_values(line)}')



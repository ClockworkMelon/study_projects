def loading(a):
    bar = '%' * a + '.' * (100 - a)

    if a == 100:
        return f'100% Complete!\n[{bar}]'
    else:
        return f'{a}% [{bar}]\nStill loading...'

load = int(input())

print(loading(load))
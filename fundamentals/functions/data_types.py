def data_type(lol, wow):

    if lol == 'int':
        a = int(wow) * 2
        print(f'{a}')
    elif lol == 'real':
        try:
            a = int(wow) * 1.5
            print(f'{a:.2f}')
        except ValueError:
            a = float(wow) * 1.5
            print(f'{a:.2f}')
    elif lol == 'string':
        print(f'${wow}$')

command = input()
a_variable = input()

data_type(command, a_variable)
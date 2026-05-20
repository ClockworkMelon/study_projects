command = input()
coffee = 0
commands = ['MOVIE', 'CODING', 'CAT', 'DOG', 'movie', 'coding', 'cat', 'dog']

while command != 'END' and coffee <= 5:
    if command in commands and command.islower():
        coffee += 1
    elif command in commands and command.isupper():
        coffee += 2

    command = input()

if coffee <= 5:
    print(coffee)
else:
    print(f'You need extra sleep')
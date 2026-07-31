dictionary = {}
number_of_lines = 0

while True:
    entry = input().split("-")
    if entry[0].isdigit():
        number_of_lines = int(entry[0])
        break

    name = entry[0]
    number = entry[1]
    dictionary[name] = number

phonebook_name_search = [input() for _ in range(number_of_lines)]

for name in phonebook_name_search:
    if name in dictionary:
        print(f'{name} -> {dictionary[name]}')
    else:
        print(f'Contact {name} does not exist.')



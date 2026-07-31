num = int(input())
zero_or_one = int(input())

binary = bin(num)[2:]
counter = 0

for char in binary:
    if int(char) == zero_or_one:
        counter += 1

print(f'{num} -> {binary}')
char_representation = ''

if zero_or_one == 0:
    char_representation = "zeroes"
else:
    char_representation = 'ones'

print(f'We have {counter} {char_representation}.')
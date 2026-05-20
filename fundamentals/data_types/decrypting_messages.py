key = int(input())
letters_count = int(input())

for let in range(letters_count):
    letter = input()
    p = ord(letter) + key
    print(f'{chr(p)}', end='')

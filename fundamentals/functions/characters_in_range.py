def sequence(a, b):
    ascii_list = []
    for x in range(ord(a) + 1, ord(b)):
        code = chr(x)
        ascii_list.append(code)
    return ascii_list

first = input()
second = input()

print(' '.join(sequence(first, second)))
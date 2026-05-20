chars_count = int(input())
sum = 0
for ch in range(chars_count):
    char = input()
    sum += ord(char)

print(f'The sum equals: {sum}')
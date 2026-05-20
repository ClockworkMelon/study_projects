n = int(input())
sums = 0
for _ in range(1, n + 1):
    char = input()

    sums += ord(char)

print(f'The sum equals: {sums}')
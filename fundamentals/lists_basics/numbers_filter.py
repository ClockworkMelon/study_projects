n = int(input())
numbers = []
filter_nums = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

command = input()

for num in numbers:
    if command == 'even':
        if num % 2 == 0 or num == 0:
            filter_nums.append(num)
    elif command == 'odd':
        if num % 2 != 0:
            filter_nums.append(num)
    elif command == 'positive':
        if num >= 0:
            filter_nums.append(num)
    elif command == 'negative':
        if num < 0:
            filter_nums.append(num)

print(filter_nums)
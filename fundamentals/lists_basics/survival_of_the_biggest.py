numbers_str = list(map(int, input().split(' ')))
removals_count = int(input())

for _ in range(removals_count):
    lowest_num = min(numbers_str)
    numbers_str.remove(lowest_num)

survived_nums = ', '.join(map(str, numbers_str))

print(survived_nums)
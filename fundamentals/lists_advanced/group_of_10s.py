nums_group = list(map(int, input().split(", ")))
tens = 10

while sum(nums_group) > 0:
    tens_group = []
    for num in range(len(nums_group)):
        if tens >= nums_group[num] > 0:
            tens_group.append(nums_group[num])
            nums_group[num] = 0

    print(f'Group of {tens}\'s: {tens_group}')
    tens += 10
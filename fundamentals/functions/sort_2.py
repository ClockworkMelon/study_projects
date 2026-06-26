def sorted_():
    sorted_nums = [x for x in nums]
    sorted_nums.sort()

    return sorted_nums

nums = [int(x) for x in input().split(' ')]

print(sorted_())
nums = list(map(int, input().split(', ')))
idexes = []
for x, y in enumerate(nums):
    if int(y) % 2 == 0:
        idexes.append(x)

print(idexes)

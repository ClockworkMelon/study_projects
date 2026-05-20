nums = list(map(int, input().split(', ')))

result = []
zeros = 0

for n in nums:
    if n == 0:
        zeros += 1
    else:
        result.append(n)

result.extend([0] * zeros)

print(result)
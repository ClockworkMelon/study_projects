numbers = [int(x) for x in input().split(', ')]
beggars = int(input())

result = []

for beggar_index in range(beggars):
    current_sum = 0
    for i in range(beggar_index, len(numbers), beggars):
        current_sum += numbers[i]
    result.append(current_sum)

print(result)
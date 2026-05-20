n = int(input())
positive = []
negative = []

for _ in range(n):
    num = int(input())

    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)


positive_count = len(positive)
negative_count = sum(negative)

print(positive)
print(negative)
print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {negative_count}')
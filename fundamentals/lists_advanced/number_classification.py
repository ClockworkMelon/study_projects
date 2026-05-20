string = list(map(int, input().split(', ')))
positive = []
negative = []
even = []
odd = []

for x in string:
    if x >= 0:
        positive.append(x)
    else:
        negative.append(x)

    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(f'Positive: {", ".join(str(x) for x in positive)}')
print(f'Negative: {", ".join(str(x) for x in negative)}')
print(f'Even: {", ".join(str(x) for x in even)}')
print(f'Odd: {", ".join(str(x) for x in odd)}')
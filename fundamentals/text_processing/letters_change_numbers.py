string_line = input().split()
total = 0

for combination in string_line:
    number = int(combination[1:-1])
    current_total = 0
    if combination[0].isupper():
        current_total += number / (ord(combination[0]) - 64)
    else:
        current_total += number * (ord(combination[0]) - 96)

    if combination[-1].isupper():
        current_total -= ord(combination[-1]) - 64
    else:
        current_total += ord(combination[-1]) - 96

    total += current_total

print(f"{total:.2f}")
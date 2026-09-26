numbers = [float(x) for x in input().split()]

counts = {}
order = []

for num in numbers:
    if num not in counts:
        order.append(num)      # пазим реда на първа поява
    counts[num] = counts.get(num, 0) + 1

for num in order:
    print(f"{num:.1f} - {counts[num]} times")

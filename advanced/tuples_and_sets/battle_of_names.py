number_of_names = int(input())
odd_set = set()
even_set = set()

for row in range(1, number_of_names + 1):
    name = input()

    name_value = 0
    for character in name:
        name_value += ord(character)

    name_value = int(name_value / row)

    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    output = odd_set.union(even_set)
elif sum_odd > sum_even:
    output = odd_set.difference(even_set)
else:
    output = odd_set.symmetric_difference(even_set)

print(", ".join(str(x) for x in output))


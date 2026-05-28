factor = int(input())
count = int(input())
list_of_multiples = []

for i in range(count):
    if len(list_of_multiples) == 0:
        list_of_multiples.append(factor)
    else:
        list_of_multiples.append(list_of_multiples[i - 1] + factor)

print(list_of_multiples)
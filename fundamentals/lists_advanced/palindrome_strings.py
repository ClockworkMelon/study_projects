pals = list(map(str, input().split(' ')))
srch_pal = input()
pal_count = 0
pals_two = []

for x in pals:
    if x == srch_pal:
        pal_count += 1

    if x == "".join(reversed(str(x))):
        pals_two.append(x)

print(f'{pals_two}')
print(f'Found palindrome {pal_count} times')
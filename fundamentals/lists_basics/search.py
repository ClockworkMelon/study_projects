rows = int(input())
word = input()
listi = []
listi_2 = []

for _ in range(rows):
    strings = input()
    listi.append(strings)

    if word in strings:
        listi_2.append(strings)

print(listi)
print(listi_2)
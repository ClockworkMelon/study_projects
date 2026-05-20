n = int(input())

while True:
    n += 1
    if len(str(n)) == len(set(str(n))):
        break

print(n)

from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
honey_operators = [x for x in input().split()][::-1]

total_honey = 0
while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if bee <= nectar:
        symbol = honey_operators.pop()
        if symbol == "+":
            total_honey += abs(bee + nectar)
        elif symbol == "-":
            total_honey += abs(bee - nectar)
        elif symbol == "*":
            total_honey += abs(bee * nectar)
        elif symbol == "/":
            if nectar > 0:
                total_honey += abs(bee / nectar)
    elif bee > nectar:
        bees.appendleft(bee)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(y) for y in nectars)}")
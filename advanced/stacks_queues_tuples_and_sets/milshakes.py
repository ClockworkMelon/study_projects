from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(y) for y in input().split(", "))

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:

    choco = chocolates.pop()        
    milk = cups_of_milk.popleft()

    if choco <= 0 and milk <= 0:
        continue
    if choco <= 0:
        cups_of_milk.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(choco)
        continue

    if choco == milk:
        milkshakes += 1
    else:
        chocolates.append(choco - 5)
        cups_of_milk.append(milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")

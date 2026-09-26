from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]
wasted_water = 0

cups_filled = False
no_bottles_left = False

while cups and bottles:
    current_cup = cups.popleft()

    while current_cup > 0:
        if bottles:
            current_bottle = bottles.pop()
        else:
            break

        if current_cup >= current_bottle:
            current_cup -= current_bottle
        elif current_cup < current_bottle:
            wasted_water += current_bottle - current_cup
            current_cup = 0

    if not cups:
        cups_filled = True
    elif not bottles:
        no_bottles_left = True

if cups_filled:
    print(f'Bottles: {" ".join(map(str, bottles[::-1]))}')
elif no_bottles_left:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f'Wasted litters of water: {wasted_water}')
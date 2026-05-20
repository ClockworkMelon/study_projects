import math as m

group_size = int(input())
days_total = int(input())
day = 0
coins = 0
while True:
    day += 1

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    if day % 3 == 0:
        coins -= 3 * group_size
        if day % 5 == 0:
            coins -= 2 * group_size

    if day % 5 == 0:
        coins += 20 * group_size

    coins += 50 - (2 * group_size)
    if day == days_total:
        break

coin_split = m.floor(coins / group_size)

print(f'{group_size} companions received {coin_split} coins each.')
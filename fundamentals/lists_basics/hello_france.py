import re

item_list = input().split('|')
budget = float(input())

item, price = zip(*([re.split('->', f) for f in item_list]))
prices = list(map(float, price))
sale_prices = []
bought_prices = []

for thing, cena in zip(item, prices):
    if thing == "Clothes":
        if cena <= 50.00 and budget >= cena:
            budget -= cena
        else:
            continue
    elif thing == 'Shoes':
        if cena <= 35.00 and budget >= cena:
            budget -= cena
        else:
            continue
    elif thing == 'Accessories':
        if cena <= 20.50 and budget >= cena:
            budget -= cena
        else:
            continue
    bought_prices.append(cena)
    sale_prices.append(cena + (cena * 0.4))

profit = sum(sale_prices) - sum(bought_prices)
new_budget = budget + sum(sale_prices)

print(f'{" ".join(f"{x:.2f}" for x in sale_prices)}')
print(f'Profit: {profit:.2f}')

if new_budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
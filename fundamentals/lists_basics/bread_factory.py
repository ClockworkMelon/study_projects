import re

events = input().split('|')
energy = 100
coins = 100

event, energy_price = zip(*([re.split('-', f) for f in events]))
energy_price = list(map(int, energy_price))
is_pass = True

for sluchka, cifra in zip(event, energy_price):
    if sluchka == 'rest':
        gained = min(100 - energy, cifra)
        energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')
    elif sluchka == 'order':
        if energy >= 30:
            energy -= 30
            coins += cifra
            print(f'You earned {cifra} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= cifra:
            coins -= cifra
            print(f'You bought {sluchka}.')
        else:
            print(f'Closed! Cannot afford {sluchka}.')
            is_pass = False
            break

if is_pass:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
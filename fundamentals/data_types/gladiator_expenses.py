loses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = 0
sword = 0
shield = 0
armor = 0
loss = 0
shield_counter = 0

for _ in range(loses):
    loss += 1

    while not (loss % 2 == 0 and loss % 3 == 0):

        if loss % 2 == 0:
            helmet += 1

        if loss % 3 == 0:
            sword += 1

        break
    else:
        helmet += 1
        sword += 1
        shield += 1
        shield_counter += 1

    if shield_counter == 2:
        armor += 1
        shield_counter = 0

helmet_price_total = helmet_price * helmet
sword_price_total = sword_price * sword
shield_price_total = shield_price * shield
armor_price_total = armor_price * armor

total = helmet_price_total + sword_price_total + shield_price_total + armor_price_total

print(f'Gladiator expenses: {total:.2f} aureus')


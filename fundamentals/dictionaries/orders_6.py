dictionary = {}

while True:
    order = input().split()

    if order[0] == "buy":
        break
    else:
        beveridge = order[0]
        price = float(order[1])
        quantity = int(order[2])

    if beveridge not in dictionary:
        dictionary[beveridge] = {price: quantity}
    else:
        current_price = list(dictionary[beveridge].keys())[0]
        current_quantity = dictionary[beveridge][current_price]

        new_quantity = quantity + current_quantity

        if price != current_price:
            dictionary[beveridge] = {price: new_quantity}
        else:
            dictionary[beveridge][price] = new_quantity

for prime_key in dictionary:
    for key, value in dictionary[prime_key].items():
        cost = float(key) * int(value)
        print(f'{prime_key} -> {cost:.2f}')


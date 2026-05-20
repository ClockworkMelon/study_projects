def coffee_shop(product, quantity):
    products = ["coffee", "coke", "water", "snacks"]
    prices = [1.50, 1.40, 1.00, 2.00]

    product_index = products.index(product)
    price_index = product_index

    price = prices[price_index] * quantity

    return price

prod = input()
col = int(input())

print(f'{coffee_shop(prod, col):.2f}')

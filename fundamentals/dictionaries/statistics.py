# products = {}
#
# while True:
#     items = input().split(": ")
#
#     if items[0] == "statistics":
#         break
#
#     com_one = items[0]
#     com_two = int(items[1])
#
#     if com_one not in products:
#         products[com_one] = com_two
#     elif com_one in products:
#         products[com_one] += com_two
#
# print(f'Products in stock:\n')
#
# for key, value in products.items():
#     print(f'- {key}: {value}')
#
# print(f'Total Products: {len(products)}')
# print(f'Total Quantity: {sum(products.values())}')

class Products:
    product_inventory = {}

    def __init__(self, product: str, quantity: int):
        self.product = product
        self.quantity = quantity

    def dict_appender(self):
        if self.product not in Products.product_inventory:
            Products.product_inventory[self.product] = self.quantity
        else:
            Products.product_inventory[self.product] += self.quantity

elements = input()

while elements != 'statistics':
    tokens = elements.split(": ")
    prod = tokens[0]
    quant = int(tokens[1])
    elements = input()

    products = Products(prod, quant)
    products.dict_appender()

print(f'Products in stock:')
for key, value in Products.product_inventory.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(Products.product_inventory)}')
print(f'Total Quantity: {sum(Products.product_inventory.values())}')






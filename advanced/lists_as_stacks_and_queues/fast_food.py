food_quantity = int(input())
orders = [int(x) for x in input().split()]

print(f'{max(orders)}')

for _ in range(len(orders)):
    if orders[0] <= food_quantity:
        food_quantity -= orders[0]
        orders.remove(orders[0])
    else:
        break

if not orders:
    print(f'Orders complete')
else:
    print(f'Orders left: {" ".join(str(x) for x in orders)} ')


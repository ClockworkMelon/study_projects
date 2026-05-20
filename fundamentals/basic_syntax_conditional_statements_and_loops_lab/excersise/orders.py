orders = int(input())
total = 0
for order in range(1, orders + 1):
    price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price <= 100.00 or not 1 <= days <= 31 or not 1 <= capsules_per_day <= 2000:
        continue
    else:
        order_total = (price * capsules_per_day) * days
        total += order_total

        print(f'The price for the coffee is: ${order_total:.2f}')

print(f'Total: ${total:.2f}')
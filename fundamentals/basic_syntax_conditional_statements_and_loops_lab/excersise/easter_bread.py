budget = float(input())
flour_price = float(input())
# recepie
# loaf is 1kg flour 1 pack eggs 0.25 milk
current_loafs_count = 0
current_colored_eggs = 0

eggs_price = flour_price * 0.75
milk_price_per_loaf = (flour_price * 1.25) / 4
price_per_loaf = eggs_price + milk_price_per_loaf + flour_price

while price_per_loaf < budget:
    current_loafs_count += 1
    current_colored_eggs += 3
    budget -= price_per_loaf

    if current_loafs_count % 3 == 0:
        current_colored_eggs -= (current_loafs_count - 2)

print(f'You made {current_loafs_count} loaves of Easter bread! Now you have {current_colored_eggs} eggs and '
      f'{budget:.2f}BGN left.')

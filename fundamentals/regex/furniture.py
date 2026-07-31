import re

bought_furniture = []
total_cost = 0

command = input()
pattern = r">>(\w+)<<(\d+\.\d+|\d+)!(\d+)"

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture_name = match.group(1)
        price = match.group(2)
        quantity = match.group(3)

        bought_furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)
    command = input()

print(f'Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")

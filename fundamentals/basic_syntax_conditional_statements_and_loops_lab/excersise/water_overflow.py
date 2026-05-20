pours = int(input())
capacity = 255
poured = 0
for p in range(pours):
    litres_of_water = int(input())

    if poured + litres_of_water <= capacity:
        poured += litres_of_water
    else:
        print(f'Insufficient capacity!')

print(f'{poured}')
import re
fire = input().split('#')
water = int(input())
fire_level, water_needed = zip(*([re.split(' = ', f) for f in fire]))
water_n = list(map(int, water_needed))
effort = 0
total_fire = 0
valid_water = []

for i in range(len(fire)):
    if fire_level[i] == 'High':
        if 81 <= water_n[i] <= 125 and water >= water_n[i]:
            water -= water_n[i]
        else:
            continue
    elif fire_level[i] == 'Medium':
        if 51 <= water_n[i] <= 80 and water >= water_n[i]:
            water -= water_n[i]
        else:
            continue
    elif fire_level[i] == 'Low':
        if 1 <= water_n[i] <= 50 and water >= water_n[i]:
            water -= water_n[i]
        else:
            continue

    valid_water.append(water_n[i])
    effort += water_n[i] * 0.25
    total_fire += water_n[i]

    if water <= 0:
        break

print(f'Cells: ')
for b in valid_water:
    print(f'- {b}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
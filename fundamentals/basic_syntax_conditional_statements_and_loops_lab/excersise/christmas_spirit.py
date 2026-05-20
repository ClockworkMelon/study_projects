decorations_quantity = int(input())
days_left = int(input())
cost = 0
spirit = 0

# Decoration    Price/Piece Points/Shopping
#
# Ornament Set      2$               5
#
# Tree Skirt        5$               3
#
# Tree Garland      3$               10
#
# Tree Lights       15$              17

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decorations_quantity += 2

    if day % 2 == 0:
        cost += ornament_set * decorations_quantity
        spirit += 5

    if day % 3 == 0:
        cost += (tree_skirt + tree_garland) * decorations_quantity
        spirit += 13

    if day % 5 == 0:
        cost += tree_lights * decorations_quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30

    if day % 10 == 0:
        cost += tree_lights + tree_garland + tree_skirt
        spirit -= 20

if days_left % 10 == 0:
    spirit -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')
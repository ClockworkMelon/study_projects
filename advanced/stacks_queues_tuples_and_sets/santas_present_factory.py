from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(y) for y in input().split())

crafting_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted = []

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()

    if material == 0 and magic == 0:
        continue

    if material == 0:
        magic_levels.appendleft(magic)
        continue

    if magic == 0:
        materials.append(material)
        continue

    total_magic = material * magic

    if total_magic < 0:
        materials.append(material + magic)
        continue

    if total_magic in crafting_table:
        crafted.append(crafting_table[total_magic])
        continue

    if total_magic > 0:
        materials.append(material + 15)

if ("Doll" in crafted and "Wooden train" in crafted) or \
   ("Teddy bear" in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for toy in sorted(set(crafted)):
    print(f"{toy}: {crafted.count(toy)}")



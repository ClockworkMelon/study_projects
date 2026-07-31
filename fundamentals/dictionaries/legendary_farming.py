
dictionary = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
legendary_obtained = False

while not legendary_obtained:
    quantity_and_materials = input().split()

    for i in range(0, len(quantity_and_materials), 2):
        key = quantity_and_materials[i + 1].lower()
        value = quantity_and_materials[i]
        if key in dictionary:
            dictionary[key] += int(value)
        else:
            if key not in junk:
                dictionary[key] = int(value)
            else:
                dictionary[key] += int(value)

        if dictionary["motes"] >= 250:
            print(f'Dragonwrath obtained!')
            dictionary["motes"] -= 250
            legendary_obtained = True
            break

        elif dictionary["fragments"] >= 250:
            print(f'Valanyr obtained!')
            dictionary["fragments"] -= 250
            legendary_obtained = True
            break

        elif dictionary['shards'] >= 250:
            print(f'Shadowmourne obtained!')
            dictionary["shards"] -= 250
            legendary_obtained = True
            break

for key, value in dictionary.items():
    print(f'{key}: {value}')

for key, value in junk.items():
    print(f'{key}: {value}')
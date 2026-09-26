sentence = input()

occurrences_dict = {}

for character in sentence:
    if character not in occurrences_dict:
        occurrences_dict[character] = 1
    else:
        occurrences_dict[character] += 1

occurrences_list = sorted(occurrences_dict)
for element in occurrences_list:
    print(f"{element}: {occurrences_dict[element]} time/s")
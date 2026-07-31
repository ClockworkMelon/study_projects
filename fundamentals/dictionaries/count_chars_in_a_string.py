text = [x for x in input() if x != " "]
dictionary = {}

for char in text:
    if char not in dictionary:
        dictionary[char] = 0
    dictionary[char] += 1

for key, value in dictionary.items():
    print(f'{key} -> {value}')

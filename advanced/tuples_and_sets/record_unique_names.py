number_of_names = int(input())
names = []

for name in range(number_of_names):
    name_record = input()
    names.append(name_record)

unique_names = set(names)

for name in unique_names:
    print(name)


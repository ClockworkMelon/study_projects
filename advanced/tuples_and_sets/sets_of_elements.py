first_set, second_set = input().split()

first_set_of_elements = set()
second_set_of_elements = set()

for _ in range(int(first_set)):
    first_set_of_elements.add(input())

for _ in range(int(second_set)):
    second_set_of_elements.add(input())

intersected_elements = first_set_of_elements.intersection(second_set_of_elements)

for element in intersected_elements:
    print(element)
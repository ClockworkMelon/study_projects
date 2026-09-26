first_number_sequence = {int(x) for x in input().split()}
second_number_sequence = {int(x) for x in input().split()}

rows = int(input())

for row in range(rows):
    instructions = input()
    action = ''
    sub_action = ''

    if instructions == "Check Subset":
        is_subset = False
        if first_number_sequence.issubset(second_number_sequence):
            is_subset = True
        elif second_number_sequence.issubset(first_number_sequence):
            is_subset = True
        print(is_subset)
        continue
    else:
        instructions = instructions.split()
        action = instructions[0]
        sub_action = instructions[1]

    new_numbers = {int(x) for x in instructions[2:]}

    if action == "Add":
        if sub_action == "First":
            first_number_sequence.update(new_numbers)
        elif sub_action == "Second":
            second_number_sequence.update(new_numbers)
    elif action == "Remove":
        if sub_action == "First":
            first_number_sequence.difference_update(new_numbers)
        elif sub_action == "Second":
            second_number_sequence.difference_update(new_numbers)

first_number_sequence = sorted(list(first_number_sequence))
second_number_sequence = sorted(list(second_number_sequence))

print(", ".join(str(x) for x in first_number_sequence))
print(", ".join(str(y) for y in second_number_sequence))
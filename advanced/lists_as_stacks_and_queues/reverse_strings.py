input_string = [x for x in input().split(" ")]
new_input = []

for word in input_string:
    new_input.append(word[::-1])

new_input = new_input[::-1]

print(" ".join(new_input))

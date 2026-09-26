mathematical_equation = input()
stack = []
for index, symbol in enumerate(mathematical_equation):
    if symbol == "(":
        stack.append(index)
    elif symbol == ")":
        start = stack.pop()
        print(mathematical_equation[start:index + 1])

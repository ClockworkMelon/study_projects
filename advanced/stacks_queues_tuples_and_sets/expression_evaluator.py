number_to_evaluate = input().split()

result_list = []
result = int(number_to_evaluate.pop(0))

for element in number_to_evaluate:
    if element.isdigit() or element.lstrip('-').isdigit():
        result_list.append(int(element))
    else:
        for target in result_list:
            if element == "-":
                result -= target
            elif element == "+":
                result += target
            elif element == "*":
                result *= target
            elif element == "/":
                result = int(result / target)
        result_list.clear()

print(result)
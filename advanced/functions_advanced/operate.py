def operate(operator, *args):
    result = args[0]
    for i in range(1, len(args)):
        if operator == "+":
            result += args[i]
        elif operator == "-":
            result -= args[i]
        elif operator == "*":
            result *= args[i]
        elif operator == "/":
            if args[i] != 0:
                result /= args[i]
    return result

print(operate("*", 3, 4))
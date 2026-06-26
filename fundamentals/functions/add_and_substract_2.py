def subtract(c: int):
    result_a = addition - c
    return result_a


def add(a: int, b:int):
    result = a + b
    return result

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

addition = add(num_1, num_2)
subtraction = subtract(num_3)

print(subtraction)
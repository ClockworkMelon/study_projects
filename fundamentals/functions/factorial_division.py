def factorial_division(a, b):
    x = a
    y = b
    for j in range(1, a):
        x *= j

    for i in range(1, b):
        y *= i

    c = x / y

    return c

num_1 = int(input())
num_2 = int(input())

print(f'{factorial_division(num_1, num_2):.2f}')
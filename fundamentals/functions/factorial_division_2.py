def factorial_division(num_one, num_two):
    num_one_factorial = num_one
    num_two_factorial = num_two

    for j in range(1, num_one):
        num_one_factorial *= j

    for i in range(1, num_two):
        num_two_factorial *= i

    division_of_the_factorials = num_one_factorial / num_two_factorial

    return division_of_the_factorials

num_1 = int(input())
num_2 = int(input())

print(f'{factorial_division(num_1, num_2):.2f}')
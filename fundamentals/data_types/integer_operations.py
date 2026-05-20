import math as m
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

op_1 = num_1 + num_2
op_2 = m.floor(op_1 / num_3)
op_3 = op_2 * num_4

print(f'{round(op_3)}')
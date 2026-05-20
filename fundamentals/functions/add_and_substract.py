def sum_numbers(a, b):
    return  a + b

def subtract(result, c):
    return result - c

def add_and_subtract(a, b, c):
    summed = sum_numbers(a, b)
    subtracted = subtract(summed, c)
    print(subtracted)

a = int(input())
b = int(input())
c = int(input())

add_and_subtract(a, b, c)



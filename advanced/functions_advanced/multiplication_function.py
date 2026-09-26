def multiply(*value):
    result = 1
    for val in value:
        result *= val
    return result

print(multiply(2, 0, 1000, 500))
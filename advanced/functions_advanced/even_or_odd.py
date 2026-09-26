def even_odd(*args):
    result = [int(x) for x in args[:-1] if int(x) % 2 == (0 if args[-1] == "even" else 1)]
    return result




print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
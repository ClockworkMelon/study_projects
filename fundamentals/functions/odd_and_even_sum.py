def odd_and_even_sum(a):
    evens = []
    odds = []
    for _, x in enumerate(a):
        if int(x) % 2 == 0:
            evens.append(int(x))
        else:
            odds.append(int(x))

    print(f'Odd sum = {sum(odds)}, Even sum = {sum(evens)}')


num_str = input()

odd_and_even_sum(num_str)
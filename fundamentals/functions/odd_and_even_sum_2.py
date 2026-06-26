def odd_even():
    odd_list = []
    even_list = []
    for x in number_to_str:
        x = int(x)
        if x % 2 != 0:
            odd_list.append(x)
        else:
            even_list.append(x)

    return [sum(odd_list), sum(even_list)]

number_to_str = [x for x in input()]

odd_even_sum = odd_even()

print(f"Odd sum = {odd_even_sum[0]}, Even sum = {odd_even_sum[1]}")
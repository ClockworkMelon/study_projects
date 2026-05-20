n = int(input())
special_numbers = [5,7, 11]
for num in range(1, n + 1):
    if num in special_numbers and num < 10:
        print(f'{num} -> True')
    elif num not in special_numbers and num < 10:
        print(f'{num} -> False')
    else:
        if num >= 10:
            num_to_str = str(num)
            if (int(num_to_str[0]) + int(num_to_str[1])) in special_numbers:
                print(f'{num} -> True')
            else:
                print(f'{num} -> False')


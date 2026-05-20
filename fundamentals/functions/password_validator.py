def is_pass_valid(a):
    is_valid = False

    while not is_valid:
        length = False
        letters = False
        digits = False
        check_list = []
        check_nums = []

        if 6 <= len(a) <= 10:
            length = True
        else:
            print('Password must be between 6 and 10 characters')

        for x in range(len(a)):
            if a[x].isalnum():
                check_list.append(a[x])
            if a[x].isdigit():
                check_nums.append(a[x])

        if len(check_list) == len(a):
            letters = True

        if len(check_nums) >= 2:
            digits = True

        if not letters:
            print('Password must consist only of letters and digits')

        if not digits:
            print('Password must have at least 2 digits')

        if length and letters and digits:
            is_valid = True
            print('Password is valid')
        else:
            break

password = input()

is_pass_valid(password)


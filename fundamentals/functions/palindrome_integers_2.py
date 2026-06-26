def palindromes(): # str_of_nums
    for i in str_of_nums:
        if i == "".join(reversed(i)):
            b = True
        else:
            b = False

        print(b)

    return None


str_of_nums = [x for x in input().split(', ')]

palindromes()
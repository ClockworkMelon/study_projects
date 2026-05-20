def palindrome(a):
    for i, x in enumerate(a):
        if str(x) == ''.join(reversed(str(x))):
            b = True
        else:
            b = False

        print(b)


integers = list(map(int, input().split(", ")))

palindrome(integers)
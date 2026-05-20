# 1.	Number Definer
# Write a program that reads a floating-point number and:
# -	prints "zero" if the number is zero
# -	prints "positive" or "negative"
# -	adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds
# 1 000 000

def is_negative_or_positive(self):
    if num < 0:
        return 'negative'
    else:
        return 'positive'

num = float(input())

num_str = ''

if num == 0:
    num_str = "zero"
elif 1 > abs(num) != 0:
    num_str = "small"
elif abs(num) > 1000000:
    num_str = 'large'

if num_str == 'zero':
    print('zero')
else:
    print(f'{num_str} {is_negative_or_positive(num)}')
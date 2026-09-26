def sum_nums(*args):
    positive = sum([x for x in args if x > 0])
    negative = sum([x for x in args if x < 0])

    return negative, positive

n, p = sum_nums(*map(int, input().split()))  #n, p = sum_nums(*[int(x) for x in input().split()])

print(n)
print(p)
if abs(n) > p:
    print("The negatives are stronger than the positives")
elif p > abs(n):
    print("The positives are stronger than the negatives")


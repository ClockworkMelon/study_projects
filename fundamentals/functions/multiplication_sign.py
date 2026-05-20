def pos_or_neg(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"

    negatives = 0
    for x in (a, b, c):
        if x < 0:
            negatives += 1

    if negatives % 2 == 0:
        return "positive"
    else:
        return "negative"

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(pos_or_neg(n1, n2, n3))
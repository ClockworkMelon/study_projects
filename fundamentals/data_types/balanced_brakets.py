n = int(input())
balance = 0
pairs = 0
valid = True

for _ in range(n):
    s = input()

    if s == "(":
        balance += 1
    elif s == ")":
        balance -= 1
        if balance < 0:
            valid = False
        pairs += 1

if valid and balance == 0 and pairs == 1:
    print("BALANCED")
else:
    print("UNBALANCED")
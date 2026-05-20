def perfect_number(n):
    divisors_sum = 0

    for d in range(1, n):
        if n % d == 0:
            divisors_sum += d

    if divisors_sum == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(perfect_number(num))
num = int(input())

divisors = [x for x in range(1, num) if num % x == 0]

message = (lambda x: 'We have a perfect number!' if sum(divisors) == num else "It's not so perfect.")(num)

print(message)
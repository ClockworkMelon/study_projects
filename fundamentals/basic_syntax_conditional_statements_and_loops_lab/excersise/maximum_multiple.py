divisor = int(input())
limit = int(input())
biggest = 0
for i in range(1, limit + 1):
    if i > biggest:
        if i % divisor == 0 and i <= limit:
            biggest = i

print(biggest)

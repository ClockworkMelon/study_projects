numbers = int(input())

odd = 0
for _ in range(numbers):
    num = int(input())
    if num % 2 == 1:
        odd = num
        break

if odd == 0:
    print("All numbers are even.")
else:
    print(f"{odd} is odd!")

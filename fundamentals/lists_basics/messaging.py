numbers = list(map(int, input().split()))
text = list(input())
message = ""

for num in numbers:
    index = sum(int(d) for d in str(num))
    index %= len(text)  # wrap around
    message += text.pop(index)

print(message)
letters = int(input())

for i in range(0, letters):
    for j in range(0, letters):
        for y in range(0, letters):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + y)}')
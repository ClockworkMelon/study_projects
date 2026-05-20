string = input().split(", ")

string.sort(key=lambda x: (-len(x), x))

print(string)
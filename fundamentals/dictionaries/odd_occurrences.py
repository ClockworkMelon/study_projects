words = input().split()

dictionary = {}

for word in words:
    lower_case_word = word.lower()
    if lower_case_word not in dictionary:
        dictionary[lower_case_word] = 0
    dictionary[lower_case_word] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
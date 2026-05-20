word = input()
word_indexes = []
for position, letter in enumerate(word):
    if letter.isupper():
        word_indexes.append(position)

print(word_indexes)
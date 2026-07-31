
while True:
    word = input()

    if word == "end":
        break

    new_word = word[::-1]

    print(f'{word} = {new_word}')
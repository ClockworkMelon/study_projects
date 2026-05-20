word = list(map(str, input()))
new_word = []
for x in word:
    if not str(x) in "aoueiAOUIE":
        new_word.append(x)

print("".join(new_word))
forbidden_words = input().split(", ")
text_to_censor = input()

for word in forbidden_words:
    while word in text_to_censor:
        text_to_censor = text_to_censor.replace(word, "*" * len(word))

print(text_to_censor)
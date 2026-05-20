def words_in_word(text):
    words = ['sand', 'water', 'fish', 'sun']
    low_cases = text.lower()
    return sum(low_cases.count(word) for word in words )

word = input()

print(words_in_word(word))
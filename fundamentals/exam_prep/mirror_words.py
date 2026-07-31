import re
gibberish = input()
mirror_words_container = []

pattern = '@{1}([a-zA-Z]{3,})@{2}([a-zA-Z]{3,})@{1}|#{1}([a-zA-Z]{3,})#{2}([a-zA-Z]{3,})#{1}'

matches = re.findall(pattern, gibberish)

for match in re.finditer(pattern, gibberish):
    first_word = ''
    second_word = ''
    if match.group(3) and match.group(4):
        first_word = match.group(3)
        second_word = match.group(4)
    elif match.group(1) and match.group(2):
        first_word = match.group(1)
        second_word = match.group(2)

    if first_word[::-1] == second_word:
        package = first_word + " " + "<=>" + " " + second_word
        mirror_words_container.append(package)

if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print(f'No word pairs found!')

if mirror_words_container:
    print(f'The mirror words are:')
    print(", ".join(mirror_words_container))
else:
    print("No mirror words!")
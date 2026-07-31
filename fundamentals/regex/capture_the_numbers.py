import re

matches = []
text = input()

while text:

    pattern = r"\d+"
    match = re.findall(pattern, text)
    matches += match
    text = input()

print(" ".join(matches))
import re

text = input()
matches = []

while text:
    pattern = r"((www\.)([a-zA-Z0-9-]+)(\.[a-z]+)+)"
    match = re.findall(pattern, text, re.MULTILINE)
    matches += match
    text = input()

for match in matches:
    print(match[0])
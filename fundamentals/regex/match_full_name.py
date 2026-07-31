import re

name = input()

pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"
matches = re.findall(pattern, name)

print(" ".join(matches))


parentheses = input()

parentheses_list = []
pairs = {")":"(", "]":"[", "}":"{"}

is_balanced = True

for char in parentheses:
    if char in "([{":
        parentheses_list.append(char)
    else:
        if not parentheses_list or parentheses_list.pop() != pairs[char]:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
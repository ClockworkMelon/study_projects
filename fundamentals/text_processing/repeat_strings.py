word = input().split()

new_string = [word * len(word) for word in word]

print(''.join(new_string))
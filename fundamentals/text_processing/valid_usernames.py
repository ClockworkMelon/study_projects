def is_length_valid(user):
    if 3 <= len(user) <= 16:
        return True
    return False

def is_chars_valid(user):
    if not ("-" in user or "_" in user or user.isalnum()):
        return False
    return True

def no_spaces(user):
    if " " in user:
        return False
    return True

def is_username_valid(user):
    if is_length_valid(user) and is_chars_valid(user) and no_spaces(user):
        return True
    return False

usernames = input().split(', ')

for username in usernames:
    if is_username_valid(username):
        print(f'{username}')
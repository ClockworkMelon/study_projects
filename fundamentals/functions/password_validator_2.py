def is_pass_valid():
    length_validation = False
    chars_validation = False
    digits_validation = False

    if 6 <= len(password) <= 10:
        length_validation = True

    digits_count = 0
    for i in password:
        if i.isalpha():
            chars_validation = True
        elif i.isdigit():
            chars_validation = True
            digits_count += 1
            if digits_count >= 2:
                digits_validation = True
        else:
            chars_validation = False
            break

    return [length_validation, chars_validation, digits_validation]

password = input()
validations = is_pass_valid()

if False not in validations:
    print("Password is valid")
else:
    if not validations[0]:
        print("Password must be between 6 and 10 characters")
    if not validations[1]:
        print("Password must consist only of letters and digits")
    if not validations[2]:
        print("Password must have at least 2 digits")


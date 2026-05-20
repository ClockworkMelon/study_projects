while True:
    string = input()

    if string == 'End':
        break
    else:
        if not string == "SoftUni":
            new_string = []
            for i in string:
                i += i
                new_string.append(i)

            print("".join(new_string))

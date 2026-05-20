peope = int(input())
cap = int(input())

full_course = peope // cap

if peope / cap > peope // cap:
    full_course = (peope // cap) + 1
    print(full_course)
else:
    print(full_course)
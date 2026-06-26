from random import randint

def random_list_of_numbers(n):
    listche = []
    for i in range(n):
        num = randint(i, 100)
        if num % 2 == 0:
            listche.append(num)

    if len(listche) > 0:
        return listche
    else:
        return f'No even numbers generated.'


random_num = random_list_of_numbers(int(input()))


print(random_num)
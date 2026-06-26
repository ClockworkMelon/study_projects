num_list = input().split(' ')

even_num_list = [int(x) for x in filter(lambda x: int(x) % 2 == 0, num_list)]

print(even_num_list)


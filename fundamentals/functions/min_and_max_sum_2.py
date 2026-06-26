# def min_max():
#     min_num = min(str_of_nums)
#     max_num = max(str_of_nums)
#     sum_nums = sum(str_of_nums)
#
#     return [min_num, max_num, sum_nums]

str_of_nums = [int(x) for x in input().split(' ')]

# results = min_max()
#
# print(f'The minimum number is {results[0]}')
# print(f'The maximum number is {results[1]}')
# print(f'The sum number is: {results[2]}')


results = [lambda x, i , y, z: 0, min(str_of_nums), max(str_of_nums), sum(str_of_nums)]

print(f'The minimum number is {results[1]}')
print(f'The maximum number is {results[2]}')
print(f'The sum number is: {results[3]}')

#BOTH WAYS WORK NORMAL OR LAMBDA FUNCTION
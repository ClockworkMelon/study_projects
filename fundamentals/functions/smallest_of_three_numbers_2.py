def numbers(one: int, two: int, three: int):
    num_list = [one, two, three]

    return min(num_list)

num_one = int(input())
num_two = int(input())
num_three = int(input())

print(numbers(num_one, num_two, num_three))


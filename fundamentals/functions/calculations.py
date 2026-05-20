def calc(command, first_num, second_num):
    result = None
    commands = ["multiply", "divide", "add", "subtract"]

    if command == commands[0]:
        result = first_num * second_num
    elif command == commands[1]:
        result = int(first_num / second_num)
    elif command == commands[2]:
        result = first_num + second_num
    elif command == commands[3]:
        result = first_num - second_num

    return result

comm = input()
num_1 = int(input())
num_2 = int(input())

print(calc(comm, num_1, num_2))

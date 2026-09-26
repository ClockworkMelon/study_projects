starting_water = int(input())
name = input()
queue = []

while name != "Start":
    queue.append(name)
    name = input()

litters = input()
while litters != "End":
    command = litters.split()
    if len(command) == 1:
        if int(command[0]) <= starting_water and len(queue) >= 1:
            print(f'{queue[0]} got water')
            queue.pop(0)
            starting_water -= int(command[0])
        else:
            print(f'{queue[0]} must wait')
            queue.pop(0)
    elif len(command) > 1:
        amount = int(command[1])
        starting_water += amount
    litters = input()
print(f'{starting_water} liters left')

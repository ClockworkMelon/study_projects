box = [int(x) for x in input().split()]
capacity = int(input())

racks = 1
current = 0

while box:
    cloth = box.pop()
    if current + cloth <= capacity:
        current += cloth
        if current == capacity and box:
            racks += 1
            current = 0
    else:
        racks += 1
        current = cloth

print(racks)

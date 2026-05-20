rooms = int(input())
chairs_left = 0
free_chairs = True

for room in range(1, rooms + 1):
    occupancy = list(input().split())

    if len(occupancy[0]) < int(occupancy[1]):
        print(f"{abs(len(occupancy[0]) - int(occupancy[1]))} more chairs needed in room {room}")
        free_chairs = False
    else:
        chairs_left += abs(len(occupancy[0]) - int(occupancy[1]))

if free_chairs:
    print(f"Game On, {chairs_left} free chairs left")

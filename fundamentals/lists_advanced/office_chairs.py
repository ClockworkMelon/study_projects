rooms = int(input())
roomsies = [0] * rooms
free_chairs = 0
alL_rooms_not_at_capacity = True

for room in range(rooms):
    guests_chairs = input().split()

    guests = int(guests_chairs[1])
    chairs = len(guests_chairs[0])
    roomsies[room] += chairs

    if (roomsies[room] - guests) < 0:
        print(f'{abs(roomsies[room] - guests)} more chairs needed in room {room + 1} ')
        alL_rooms_not_at_capacity = False
    else:
        free_chairs += roomsies[room] - guests

if alL_rooms_not_at_capacity:
    print(f'Game On, {free_chairs} free chairs left')


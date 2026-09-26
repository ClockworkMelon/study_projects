from collections import deque

petrol_pumps_count = int(input())
pumps = deque()

for pump in range(petrol_pumps_count):
    petrol_amount, distance = [int(x) for x in input().split()]
    pumps.append((petrol_amount, distance))
print(pumps)

start = 0

while True:
    fuel = 0
    failed = False

    for petrol, distance in pumps:
        fuel += petrol
        if fuel < distance:
            failed = True
            break
        else:
            fuel -= distance

    if not failed:
        print(start)
        break

    pumps.rotate(-1)
    start += 1


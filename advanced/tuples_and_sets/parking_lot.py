number_of_cars = int(input())
cars = set()

for _ in range(number_of_cars):
    direction, car = input().split(", ")

    if direction == "IN":
        cars.add(car)
    elif direction == "OUT":
        cars.remove(car)

if cars:
    for car in cars:
        print(car)
else:
    print(f'Parking Lot is Empty')
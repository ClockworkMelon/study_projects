from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed = 0

while True:
    command = input()
    if command == "END":
        break

    if command != "green":
        cars.append(command)
        continue

    current_green = green_light

    while cars and current_green > 0:
        car = cars.popleft()
        car_length = len(car)

        if car_length <= current_green:
            current_green -= car_length
            passed += 1
        else:
            remaining = car_length - current_green

            if remaining <= free_window:
                passed += 1
            else:
                hit_index = current_green + free_window
                print("A crash happened!")
                print(f"{car} was hit at {car[hit_index]}.")
                exit()

            current_green = 0

print("Everyone is safe.")
print(f"{passed} total cars passed the crossroads.")

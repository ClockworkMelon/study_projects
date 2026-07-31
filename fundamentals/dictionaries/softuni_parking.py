number_of_cars = int(input())
parking_lot_register = {}

for car in range(number_of_cars):
    command = input().split()
    action = command[0]
    username = command[1]
    license_plate = 0

    if len(command) == 3:
        license_plate = command[2]

    if action == 'register':
        if username not in parking_lot_register:
            parking_lot_register[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == 'unregister':
        if username not in parking_lot_register:
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot_register[username]
            print(f"{username} unregistered successfully")

for key, value in parking_lot_register.items():
    print(f'{key} => {value}')
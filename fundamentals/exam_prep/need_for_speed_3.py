number_of_cars = int(input())
garage = {}

for data in range(number_of_cars):
    car, milage, fuel = input().split("|")
    garage[car] = {"milage": int(milage), 'fuel': int(fuel)}

command = input()

while command != "Stop":
    command = command.split(" : ")
    action = command[0]

    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if garage[car]['fuel'] >= fuel:
            garage[car]['milage'] += distance
            garage[car]['fuel'] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if garage[car]['milage'] >= 100000:
                del garage[car]
                print(f'Time to sell the {car}!')
        else:
            print(f'Not enough fuel to make that ride')
    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if garage[car]["fuel"] + fuel > 75:
            filled_fuel = 75 - garage[car]['fuel']
            garage[car]['fuel'] = 75
            print(f'{car} refueled with {filled_fuel} liters')
        else:
            garage[car]['fuel'] += fuel
            print(f'{car} refueled with {fuel} liters')
    elif action == 'Revert':
        car = command[1]
        kilometers = int(command[2])
        if garage[car]['milage'] - kilometers >= 10000:
            garage[car]['milage'] -= kilometers
            print(f'{car} mileage decreased by {kilometers} kilometers')
        else:
            garage[car]['milage'] = 10000
    command = input()

for car, car_info in garage.items():
    milage = car_info['milage']
    fuel = car_info['fuel']
    print(f'{car} -> Mileage: {milage} kms, Fuel in the tank: {fuel} lt.')
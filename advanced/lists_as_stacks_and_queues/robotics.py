from collections import deque

robots_input = input().split(";")
robots = []

for r in robots_input:
    name, time = r.split("-")
    robots.append([name, int(time), 0])   # [име, време за обработка, оставащо време]

start_time = list(map(int, input().split(":")))
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

hours, minutes, seconds = start_time

def format_time(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

current_time_seconds = hours * 3600 + minutes * 60 + seconds

while products:
    current_time_seconds += 1

    # Намаляваме оставащото време на роботите
    for robot in robots:
        if robot[2] > 0:
            robot[2] -= 1

    product = products.popleft()

    assigned = False
    for robot in robots:
        if robot[2] == 0:  # свободен робот
            robot[2] = robot[1]  # задаваме време за обработка
            h = (current_time_seconds // 3600) % 24
            m = (current_time_seconds % 3600) // 60
            s = current_time_seconds % 60
            print(f"{robot[0]} - {product} [{format_time(h, m, s)}]")
            assigned = True
            break

    if not assigned:
        products.append(product)  # връщаме продукта в края на опашката

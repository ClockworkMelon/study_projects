import re
gibberish = input()

pattern = r'#{1}([A-Za-z ]+[^ ])#{1}(\d{2}\/\d{2}\/\d{2})#{1}(\d+)#{1}|\|{1}([A-Za-z ]+[^ ])\|{1}(\d{2}\/\d{2}\/\d{2})[\|]{1}(\d+)\|{1}'
total_calories = 0

for food in re.finditer(pattern, gibberish):
    if food.group(3):
        total_calories += int(food.group(3))
    elif food.group(6):
        total_calories += int(food.group(6))

if total_calories > 0:
    will_last_days = total_calories // 2000
    print(f'You have food to last you for: {will_last_days} days!')
else:
    print(f'You have food to last you for: 0 days!')

for info in re.finditer(pattern, gibberish):
    if info.group(1):
        item = info.group(1)
        best_before = info.group(2)
        calories = int(info.group(3))
        print(f'Item: {item}, Best before: {best_before}, Nutrition: {calories}')
    elif info.group(4):
        item = info.group(4)
        best_before = info.group(5)
        calories = int(info.group(6))
        print(f'Item: {item}, Best before: {best_before}, Nutrition: {calories}')


# import re
#
# gibberish = input()
#
# pattern = r"(?P<sep>#|\|)(?P<item>[A-Za-z ]+)(?P=sep)(?P<date>\d{2}/\d{2}/\d{2})(?P=sep)(?P<cal>\d+)(?P=sep)"
#
# total_calories = 0
#
# for food in re.finditer(pattern, gibberish):
#     total_calories += int(food.group("cal"))
#
# days = total_calories // 2000
# print(f"You have food to last you for: {days} days!")
#
# for info in re.finditer(pattern, gibberish):
#     item = info.group("item")
#     date = info.group("date")
#     cal = int(info.group("cal"))
#     print(f"Item: {item}, Best before: {date}, Nutrition: {cal}")

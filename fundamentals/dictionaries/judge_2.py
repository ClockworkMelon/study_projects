judge_register = {}
total_points_register = {}
while True:
    data = input()

    if data == "no more time":
        break

    data_breakdown = data.split(" -> ")
    contest = data_breakdown[1]
    user = data_breakdown[0]
    points = int(data_breakdown[2])

    if contest not in judge_register.keys():
        judge_register[contest] = {}

    if user not in judge_register[contest]:
        judge_register[contest][user] = 0

    if points > judge_register[contest][user]:
        judge_register[contest][user] = points

for contest in judge_register:
    for user, points in judge_register[contest].items():
        if user not in total_points_register:
            total_points_register[user] = 0
        total_points_register[user] += points

for contest in judge_register:
    sorted_items = dict(sorted(judge_register[contest].items(), key=lambda kv: (-kv[1], kv[0])))
    print(f"{contest}: {len(judge_register[contest])} participants")
    user_number = 0
    for user, points in sorted_items.items():
        user_number += 1
        print(f"{user_number}. {user} <::> {points}")

user_rank = 0
print(f'Individual standings:')
sorted_total_points = dict(sorted(total_points_register.items(), key=lambda kv: (-kv[1], kv[0])))
for user, total_points in sorted_total_points.items():
    user_rank += 1
    print(f"{user_rank}. {user} -> {total_points}")

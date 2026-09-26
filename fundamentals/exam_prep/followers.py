followers = {}

commands = input()

while commands != "Log out":
    commands = commands.split(": ")

    action = commands[0]
    username = commands[1]

    if action == "New follower":
        if username not in followers.keys():
            followers[username] = {"likes": 0, "comments": 0}
    elif action == "Like":
        count = int(commands[2])
        if username not in followers.keys():
            followers[username] = {"likes": 0, "comments": 0}
        followers[username]["likes"] += count
    elif action == "Comment":
        if username not in followers.keys():
            followers[username] = {"likes": 0, "comments": 0}
        followers[username]['comments'] += 1
    elif action == "Blocked":
        if username in followers.keys():
            del followers[username]
        else:
            print(f'{username} doesn\'t exist.')
    commands = input()

print(f'{len(followers)} followers')
for user, users_info in followers.items():
    likes = users_info["likes"]
    comments = users_info['comments']
    total_count = likes + comments
    print(f'{user}: {total_count}')
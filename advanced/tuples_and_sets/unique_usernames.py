number_of_users = int(input())

users = set()

for user in range(number_of_users):
    username = input()
    users.add(username)

print(*users, sep="\n")

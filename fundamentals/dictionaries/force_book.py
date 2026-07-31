the_force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_side not in the_force_book:
            the_force_book[force_side] = []
        if not any(force_user in users for users in the_force_book.values()):
            the_force_book[force_side].append(force_user)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        for side, users in the_force_book.items():
            if force_user in users:
                users.remove(force_user)
                break
        if force_side not in the_force_book:
            the_force_book[force_side] = []
        the_force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


for side, users in the_force_book.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")

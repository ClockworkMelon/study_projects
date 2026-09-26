reservations = int(input())
reservation_list = []
vip_list = []
regular_list = []

for _ in range(reservations):
    reservation = input()
    reservation_list.append(reservation)

for guest in reservation_list:
    if guest[0].isdigit():
        vip_list.append(guest)
    else:
        regular_list.append(guest)

while True:
    incoming_guest = input()

    if incoming_guest == "END":
        break

    if incoming_guest[0].isdigit():
        vip_list.remove(incoming_guest)
    else:
        regular_list.remove(incoming_guest)

print(f'{len(vip_list) + len(regular_list)}')

if vip_list:
    vip_list.sort()
    for guest in vip_list:
        print(guest)

if regular_list:
    regular_list.sort()
    for guest in regular_list:
        print(guest)
electrons = int(input())
shells = []
n = 1
while electrons > 0:
    electron = 2 * (n ** 2)

    if electron < electrons:
        shells.append(electron)
        electrons -= electron
    else:
        shells.append(electrons)
        electrons = 0

    n += 1

print(shells)



dwarf_register = {}

while True:
    dwarf_stats = input()

    if dwarf_stats == "Once upon a time":
        break

    dwarf_details = dwarf_stats.split(" <:> ")

    name = dwarf_details[0]
    hat_color = dwarf_details[1]
    physics = int(dwarf_details[2])

    if hat_color not in dwarf_register.keys():
        dwarf_register[hat_color] = {}

    if name not in dwarf_register[hat_color]:
        dwarf_register[hat_color][name] = 0

    if physics > dwarf_register[hat_color][name]:
        dwarf_register[hat_color][name] = physics

for hat in dwarf_register.keys():
    dwarf_register[hat] = dict(sorted(dwarf_register[hat].items(), key=lambda kv: -kv[1]))

sorted_by_hat_len = dict(sorted(dwarf_register.items(), key=lambda kv: (max(kv[1].values()), len(kv[1])),reverse=True))

for hat in sorted_by_hat_len.keys():
    for dwarf, phys in sorted_by_hat_len[hat].items():
        print(f'({hat}) {dwarf} <-> {phys}')



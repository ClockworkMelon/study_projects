pokemons = list(map(int, input().split()))
captured_pokemons = []
last_captured = 0
when_out_of_range = 0
while len(pokemons) > 0:
    capture = int(input())

    if capture < 0:
        capture = 0
        pokemons[0] = pokemons[-1]
        when_out_of_range = pokemons[0]
    elif capture >= len(pokemons):
        capture = len(pokemons) - 1
        when_out_of_range = pokemons[-1]
        pokemons[-1] = pokemons[0]

    if when_out_of_range == 0:
        last_captured = pokemons.pop(capture)
        captured_pokemons.append(last_captured)
    else:
        captured_pokemons.append(when_out_of_range)

    for i in range(len(pokemons)):
        if when_out_of_range == 0:
            if pokemons[i] > last_captured:
                pokemons[i] -= last_captured
            elif pokemons[i] <= last_captured:
                pokemons[i] += last_captured
        elif when_out_of_range != 0:
            if pokemons[i] > when_out_of_range:
                pokemons[i] -= when_out_of_range
            elif pokemons[i] <= when_out_of_range:
                pokemons[i] += when_out_of_range

    when_out_of_range = 0

print(f'{sum(captured_pokemons)}')

population = list(map(int, input().split(', ')))
min_wealth = int(input())


if sum(population) < len(population) * min_wealth:
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            needed = min_wealth - population[i]
            richest_idx = population.index(max(population))

            population[i] += needed
            population[richest_idx] -= needed

    print(population)

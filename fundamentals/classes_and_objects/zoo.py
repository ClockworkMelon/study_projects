class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        total_animals = len(self.mammals) + len(self.birds) + len(self.fishes)
        output = ''
        if species == 'mammal':
            output = f'Mammals in {self.name}:{", ".join(self.mammals)}\nTotal animals: {total_animals}'
        elif species == 'fish':
            output = f'Fishes in {self.name}:{", ".join(self.fishes)}\nTotal animals: {total_animals}'
        elif species == 'bird':
            output = f'Birds in {self.name}:{", ".join(self.birds)}\nTotal animals: {total_animals}'
        return output

zoo_name = input()
rows = int(input())
zoo = Zoo(zoo_name)

for row in range(rows):
    spec_name = input().split()
    zoo.add_animal(spec_name[0],spec_name[1])

get_mammal_info = input()

zoo.get_info(get_mammal_info)






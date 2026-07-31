# ingredients = input().split()
# bakery = {}
#
# for i in range(0, len(ingredients), 2):
#     key = ingredients[i]
#     value = ingredients[i + 1]
#
#     bakery[key] = int(value)
#
# print(bakery)

class Bakery:

    def __init__(self, string_line):
        self.bakery = {}
        self.string_line = string_line

    def dict_creator(self):
        for i in range(0, len(self.string_line), 2):
            key = self.string_line[i]
            value = self.string_line[i + 1]

            self.bakery[key] = int(value)

        return self.bakery


bakery = Bakery(input().split())
print(bakery.dict_creator())



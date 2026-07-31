# inventory = input().split()
# inventory_request = input().split()
# inventory_dict = {}
#
# for i in range(0, len(inventory), 2):
#     key = inventory[i]
#     value = inventory[i + 1]
#     inventory_dict[key] = int(value)
#
# for item in inventory_request:
#     if item in inventory_dict:
#         print(f'We have {inventory_dict[item]} of {item} left')
#     else:
#         print(f'Sorry, we don\'t have {item}')


class Inventory:

    def __init__(self, inventory: list, inventory_request: list):
        self.inventory = inventory
        self.inventory_request = inventory_request
        self.inventory_dict = {}

    def dict_creator(self):
        for item in range(0, len(self.inventory),2):
            key = self.inventory[item]
            value = self.inventory[item + 1]
            self.inventory_dict[key] = int(value)

    def inventory_search(self):
        output = []
        for item in self.inventory_request:
            if item in self.inventory_dict:
                output.append(f'We have {self.inventory_dict[item]} of {item} left')
            else:
                output.append(f'Sorry, we don\'t have {item}')
        return "\n".join(output)

inv = Inventory(input().split(), input().split())
inv.dict_creator()

print(inv.inventory_search())







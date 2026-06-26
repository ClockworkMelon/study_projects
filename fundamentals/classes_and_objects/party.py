class Party:
    def __init__(self):
        self.rooster = []
        
    def party_time(self):

        while True:
            person = input()
            if person == "End":
                break
            else:
                self.rooster.append(person)

        return self.rooster


party_people = Party()
people = party_people.party_time()

print(f'Going: {", ".join(people)}')
print(f'Total: {len(people)}')
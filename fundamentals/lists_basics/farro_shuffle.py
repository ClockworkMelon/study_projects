cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    mid = len(cards) // 2
    left = cards[:mid]
    right = cards[mid:]

    new_deck = []
    for i in range(mid):
        new_deck.append(left[i])
        new_deck.append(right[i])

    cards = new_deck

print(cards)
queue = input().split(', ')
wolf = queue.index('wolf')
sheep_in_danger = (len(queue) - 1) - wolf

if queue[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!')






race_times = list(map(int, input().split(' ')))

mid = len(race_times) // 2
left = race_times[:mid]
right = race_times[mid + 1:]

left_time = 0
right_time = 0

for t_1 in range(len(left)):
    if left[t_1] > 0:
        left_time += left[t_1]
    else:
        left_time *= 0.8

for t_2 in range(len(right) - 1, -1, -1):
    if right[t_2] > 0:
        right_time += right[t_2]
    else:
        right_time *= 0.8

winner = ''

if left_time < right_time:
    winner = 'left'
    time = left_time
else:
    winner = 'right'
    time = right_time

print(f'The winner is {winner} with total time: {time:.1f}')
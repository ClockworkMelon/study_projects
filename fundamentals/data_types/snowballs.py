snowballs = int(input())
best_ball = 0
ball_weight = 0
ball_time = 0
ball_quality = 0

for ball in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    ball_value = (weight // time) ** quality

    if best_ball < ball_value:
        best_ball = ball_value
        ball_weight = weight
        ball_time = time
        ball_quality = quality

print(f'{ball_weight} : {ball_time} = {best_ball} ({ball_quality})')


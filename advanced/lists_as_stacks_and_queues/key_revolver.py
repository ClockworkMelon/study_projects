from collections import deque

def reloading():
    for _ in range(1, gun_barrel_size + 1):
        if bullets:
            gun_barrel_bullets.append(bullets.pop())
        else:
            break

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(y) for y in input().split())
intelligence_value = int(input())

gun_barrel_bullets = deque()
reloading()
bullets_used = 0

while True:

    if not gun_barrel_bullets and bullets:
        print("Reloading!")
        reloading()

    if not locks:
        bullet_cost = bullets_used * bullet_price
        earned_money = intelligence_value - bullet_cost
        bullets_left = len(bullets) + len(gun_barrel_bullets)
        print(f'{bullets_left} bullets left. Earned ${earned_money}')
        break

    elif not bullets and not gun_barrel_bullets:
        print(f'Couldn\'t get through. Locks left: {len(locks)}')
        break

    current_bullet = gun_barrel_bullets.popleft()
    current_lock = locks.popleft()
    bullets_used += 1
    
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")





nums = list(map(int, input().split(' ')))
k = int(input())
kill_order = []
index = 0
num = 0

while len(nums) > 0:
    index = (index + k -1) % len(nums)
    num = nums.pop(index)
    kill_order.append(num)

print(f"[{','.join(map(str, kill_order))}]")
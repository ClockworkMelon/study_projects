from math import floor as f
buiscuits_per_worker = int(input())
workers_count = int(input())
competitor_procudce = int(input())

buiscuits_produced = 0

for day in range (1, 31):

    if day % 3 == 0:
        buiscuits_produced += f((buiscuits_per_worker * workers_count) * 0.75)
    else:
        buiscuits_produced += f(buiscuits_per_worker * workers_count)

print(f"You have produced {buiscuits_produced:.0f} biscuits for the past month.")

percentage = (abs(buiscuits_produced - competitor_procudce)/competitor_procudce) * 100

if buiscuits_produced > competitor_procudce:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
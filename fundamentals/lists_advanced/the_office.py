empl_happiness = list(map(int, input().split(' ')))
factor = int(input())

for x in range(len(empl_happiness)):
    empl_happiness[x] *= factor

avg_happiness = sum(empl_happiness) / len(empl_happiness)

happy_empl = [x for x in empl_happiness if x >= avg_happiness]

if len(happy_empl) >= (len(empl_happiness) // 2):
    print(f'Score: {len(happy_empl)}/{len(empl_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_empl)}/{len(empl_happiness)}. Employees are not happy!')
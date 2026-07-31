contests = {}
submissions_register = {}
high_score = {}

while True:
    entry = input()
    if entry == "end of contests":
        break

    entries = entry.split(":")
    contest = entries[0]
    password = entries[1]

    if contest not in contests.keys():
        contests[contest] = password

while True:
    submission = input()

    if submission == "end of submissions":
        break

    submissions = submission.split('=>')

    contest = submissions[0]
    password = submissions[1]
    username = submissions[2]
    score = int(submissions[3])

    if contest in contests:
        if password == contests[contest]:

            if username not in submissions_register.keys():
                submissions_register[username] = {}

            if contest not in submissions_register[username]:
                submissions_register[username][contest] = 0

        if username in submissions_register.keys():
            if score > submissions_register[username][contest]:
                submissions_register[username][contest] = score

for primary_key in submissions_register.keys():
    if primary_key not in high_score.keys():
        high_score[primary_key] = 0
    for subject, score in submissions_register[primary_key].items():
        high_score[primary_key] += score

print(f'Best candidate is {max(high_score)} with total {max(high_score.values())} points.')

sorted_submissions = sorted(submissions_register.keys(), key=lambda k: len(submissions_register[k]))

print('Ranking:')
for prime_key in sorted_submissions:
    sorted_inner_subs = sorted(submissions_register[prime_key].items(), key=lambda x: x[1], reverse=True)
    print(f'{prime_key}')
    for key, value in sorted_inner_subs:
        print(f'#  {key} -> {value}')


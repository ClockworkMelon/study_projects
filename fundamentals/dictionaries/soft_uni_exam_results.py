results = {}
submissions = {}

while True:
    entry = input()

    if entry == 'exam finished':
        break

    entries = entry.split('-')
    is_banned = False
    student = entries[0]
    language = ''
    score = 0

    if len(entries) == 2:
        is_banned = True
    elif len(entries) == 3:
        language = entries[1]
        score = int(entries[2])
        if language not  in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

    if student not in results.keys():
        results[student] = 0

    if is_banned:
       del results[student]
    elif score > results[student]:
        results[student] = score

print("Results:")

for student, result in results.items():
    print(f"{student} | {result}")

print("Submissions:")

for submission, count in submissions.items():
    print(f'{submission} - {count}')
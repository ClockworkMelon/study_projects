dictionary = {}
looked_for_course = ''

while True:
    command = input().split(":")

    if len(command) == 1:
        command = command[0].split('_')
        looked_for_course = " ".join(command)
        break

    name = command[0]
    student_id = int(command[1])
    course = command[2]

    if course not in dictionary:
        dictionary[course] = {}

    dictionary[course][name] = student_id

for name, student_id in dictionary[looked_for_course].items():
    print(f"{name} - {student_id}")

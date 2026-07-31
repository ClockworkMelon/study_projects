courses_library = {}

while True:
    courses_students = input().split(" : ")

    if courses_students[0] == "end":
        break

    course = courses_students[0]
    student_name = courses_students[1]

    if course not in courses_library:
        courses_library[course] = []

    courses_library[course].append(student_name)


for course_ in courses_library:
    print(f'{course_}: {len(courses_library[course_])}')
    for student in courses_library[course_]:
        print(f'-- {student}')

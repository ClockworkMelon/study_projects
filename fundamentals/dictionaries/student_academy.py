students_count = int(input())
students_grades = {}

for student in range(students_count):
    name = input()
    grade = float(input())

    if name not in students_grades:
        students_grades[name] = []

    students_grades[name].append(grade)

for stud, grad in students_grades.items():
    avg_grade = sum(students_grades[stud]) / len(students_grades[stud])

    if avg_grade >= 4.5:
        print(f'{stud} -> {avg_grade:.2f}')


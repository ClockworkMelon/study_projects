number_of_students = int(input())

student_s_grades = {}

for student in range(number_of_students):
    student_name, grade = input().split()
    if student_name not in student_s_grades:
        student_s_grades[student_name] = []
    student_s_grades[student_name].append(float(grade))

for student, grades in student_s_grades.items():
    average_grade = sum(grades) / len(grades)
    formated_grade = " ".join(f'{g:.2f}' for g in grades)
    print(f'{student} -> {formated_grade} (avg: {average_grade:.2f})')
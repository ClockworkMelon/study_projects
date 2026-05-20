def grades(grade):
    final_grade = ''
    if 2.00 <= grade <= 2.99:
        final_grade = 'Fail'
    elif 3.00 <= grade <= 3.49:
        final_grade = 'Poor'
    elif 3.50 <= grade <= 4.49:
        final_grade = 'Good'
    elif 4.50 <= grade <= 5.49:
        final_grade = 'Very Good'
    elif 5.50 <= grade <= 6.00:
        final_grade = 'Excellent'

    return final_grade

score = float(input())

print(grades(score))
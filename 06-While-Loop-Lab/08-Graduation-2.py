name_of_student = input()
grade = 1
sum_score = 0
times_failed = 0
while grade <= 12:
    score = float(input())
    if score >= 4.00:
        grade += 1
        sum_score += score
    else:
        times_failed += 1
        if times_failed > 1:
            print(f'{name_of_student} has been excluded at {grade} grade')
            break

if grade > 12:
    avg_score = sum_score / 12
    print(f'{name_of_student} graduated. Average grade: {avg_score:.2f}')

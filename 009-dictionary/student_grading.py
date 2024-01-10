def get_grade(score: int) -> str:
    grade = "Fail"

    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"

    return grade


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for student in student_scores:
    student_grades[student] = get_grade(student_scores[student])

for student in student_grades:
    print(f"{student} got a score of {student_scores[student]} which is a grade of '{student_grades[student]}'")

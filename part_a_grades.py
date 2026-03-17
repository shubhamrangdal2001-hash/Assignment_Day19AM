# Part A - Question 3
# Filter students above average and assign grades using list comprehension

def assign_grade(mark):
    if mark >= 80:
        return 'A'
    elif mark >= 60:
        return 'B'
    else:
        return 'C'


if __name__ == "__main__":
    student_marks = [45, 72, 88, 55, 91, 63, 38, 77, 84, 52]

    # compute average
    average = sum(student_marks) / len(student_marks)
    print(f"Student Marks  : {student_marks}")
    print(f"Average        : {average:.2f}")

    # filter students scoring above average using list comprehension
    above_average = [m for m in student_marks if m > average]
    print(f"Above Average  : {above_average}")

    # assign grades using list comprehension
    grades = [assign_grade(m) for m in student_marks]
    print(f"Grades         : {grades}")

    # show paired result
    print("\nMark -> Grade:")
    paired = [(m, assign_grade(m)) for m in student_marks]
    for mark, grade in paired:
        print(f"  {mark} -> {grade}")

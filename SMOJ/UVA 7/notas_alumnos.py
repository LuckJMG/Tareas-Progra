def calcular_promedio(students):
    # Variables
    tmp = list(students)
    average = []

    # Calculate average of students
    for student in tmp:
        student_average = []
        student_average.append(student[0])
        del student[0]
        student_average.append(round(sum(student) / len(student)))
        average.append(student_average)

    return average

student_grades = {'math': 85, 'science': 92, 'english': 78}

# Using items() - more readable and efficient
for subject, grade in student_grades.items():
    print(f"{subject}: {grade}")

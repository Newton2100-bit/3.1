student_grades = {'math': 85, 'science': 92, 'english': 78}

# Direct iteration - only gets keys
for subject in student_grades:
    print(subject)
# Output:
# math
# science
# english


print()
print()
# These are identical
for subject in student_grades:
    print('Directly :',subject)
print()
for subject in student_grades.keys():
    print('Keys :',subject)


print()
##Acessing the values of the dict
# Direct iteration with manual value access
for subject in student_grades:
    grade = student_grades[subject]
    print(f"{subject}: {grade}")

# 1. Given a dictionary
student_grades = {'Alice': 98, 'Bob': 85, 'Charlie': 74, 'Mike': 70}
# Print the grade of Charlie
print("Charlie's Grade:", student_grades['Charlie'])
# Update the grade of Bob to 90
student_grades['Bob'] = 90
# Add new item 'Sam:75' to the dictionary
student_grades['Sam'] = 75
# Print the total number of students
print("Total Students:", len(student_grades))
# Print all student names in the given dictionary
print("Student Names:")
for name in student_grades:
    print(name)
# 2. Given a dictionary
student_marks = {
    'Arun': {'maths': 30, 'science': 35, 'english': 40, 'history': 33},
    'Amal': {'maths': 40, 'science': 45, 'english': 48, 'history': 43},
    'Anu': {'maths': 45, 'science': 46, 'english': 47, 'history': 49}
}
# Print the mark of Amal in the subject History
print("Amal's History Mark:", student_marks['Amal']['history'])
# Update the mark of Arun in Maths to 35
student_marks['Arun']['maths'] = 35
# Print the marks of all students in all subjects
print("\nMarks of All Students:")
for student, subjects in student_marks.items():
    print(student, ":", subjects)
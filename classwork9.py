
# Write a menu-driven Python program using a class Student
# to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.



class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)


students = []

while True:
    print("\n----- STUDENT MENU -----")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Student
    if choice == 1:
        rollno = int(input("Enter roll number: "))

        found = False
        for s in students:
            if s.rollno == rollno:
                found = True
                break

        if found:
            print("Student already exists!")
        else:
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))

            student = Student(rollno, name, marks)
            students.append(student)

            print("Student added successfully!")

    # Update Marks
    elif choice == 2:
        rollno = int(input("Enter roll number: "))

        found = False
        for s in students:
            if s.rollno == rollno:
                marks = float(input("Enter new marks: "))
                s.marks = marks
                found = True
                print("Marks updated successfully!")
                break

        if not found:
            print("Student not found!")

    # Display All Students
    elif choice == 3:
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\n----- STUDENT DETAILS -----")
            for s in students:
                s.display()
                print("-------------------")

    # Search Student
    elif choice == 4:
        rollno = int(input("Enter roll number: "))

        found = False
        for s in students:
            if s.rollno == rollno:
                print("\nStudent found!")
                s.display()
                found = True
                break

        if not found:
            print("Student not found!")

    # Delete Student
    elif choice == 5:
        rollno = int(input("Enter roll number: "))

        found = False
        for s in students:
            if s.rollno == rollno:
                students.remove(s)
                found = True
                print("Student deleted successfully!")
                break

        if not found:
            print("Student not found!")

    # Exit
    elif choice == 6:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
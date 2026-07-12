Students = []

class Student:
    def __init__ (self, name, roll_number, age, marks):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.marks = marks

Exit = False
while not Exit:
    print("\nStudent Record Manager\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        student = Student(name, roll_number, age, marks)
        Students.append(student)
        print(f"Student '{name}' added to the record.")
    elif choice == '2':
        if not Students:
            print("No students in the record.")
        else:
            print("\nStudent Records:")
            for student in Students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Age: {student.age}, Marks: {student.marks}")
    elif choice == '3':
        if not Students:
            print("No students to remove.")
        else:
            roll_number = input("Enter the roll number of the student to remove: ")
            for student in Students:
                if student.roll_number == roll_number:
                    Students.remove(student)
                    print(f"Student with roll number '{roll_number}' removed from the record.")
                    break
            else:
                print(f"No student found with roll number '{roll_number}'.")
    elif choice == '4':
        Exit = True
        print("Exiting Student Record Manager.")
    else:
        print("Invalid choice. Please try again.")
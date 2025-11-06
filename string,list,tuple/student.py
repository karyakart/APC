student_names = []
student_grades = []

def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)
    print(f"Student {name} with grade {grade} added.")

def update_grade(name, new_grade):
    if name in student_names:
        index = student_names.index(name)
        student_grades[index] = new_grade
        print(f"Grade updated for {name}.")
    else:
        print("Student not found.")


def average_grade():
    if student_grades:
        avg = sum(student_grades) / len(student_grades)
        print("Average grade of class:", avg)
    else:
        print("No grades to calculate average.")


def extreme_grades():
    if student_grades:
        highest = max(student_grades)
        lowest = min(student_grades)
        print("Highest grade:", highest)
        print("Lowest grade:", lowest)
    else:
        print("No grades to find highest and lowest.")

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Display Average Grade")
    print("4. Display Highest and Lowest Grades")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(name, grade)
    elif choice == '2':
        name = input("Enter student name to update: ")
        grade = float(input("Enter new grade: "))
        update_grade(name, grade)
    elif choice == '3':
        average_grade()
    elif choice == '4':
        extreme_grades()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
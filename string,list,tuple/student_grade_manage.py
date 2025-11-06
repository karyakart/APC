student_names = list([])
student_grades = list([])

def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)

def update_grade(name, new_grade):
    if name in student_names:
        index = student_names.index(name)
        student_grades[index] = new_grade
        print(f"Updated {name}'s grade to {new_grade}")
        print(student_grades)
    else:
        print(f"Student '{name}' not found.")

def remove_student(name):
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index)
        print(f"Removed student '{name}'")
        print(student_names)
    else:
        print(f"Student not found.")

def calculate_average():
    total = sum(student_grades)
    a= total/len(student_grades)
    print("average= ",a)


def find_extreme_grades():
    max_grade = max(student_grades)
    min_grade = min(student_grades)
    print("max_grade= ",max_grade) 
    print("min_grade= ",min_grade)


add_student("prathamesh", 100)
add_student("aditya", 96)
add_student("sahil", 85)
add_student("vishal", 78)

update_grade("prathamesh", 45)

print("name of students= ",student_names)
print("grade of students= ",student_grades)
find_extreme_grades()
calculate_average()


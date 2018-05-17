students = []


def get_students_names():
    students_names = []
    for student in students:
       # students_names.append(student)
        student_name = student["name"].title()
        students_names.append(student_name)
    return students_names


def print_students_names():
    students_names = get_students_names()
    print(students_names)


def add_student(name, student_id=332):
    student = {"name" : name, "student_id" : student_id}
    students.append(student)

"""
def save_to_file(student):
    try:
        file_ref = open("Student.txt", "a")
        file_ref.write(student + "\n")
        file_ref.close()
    except Exception:
        print("Could not save file")


def read_from_file():
    try:
        file_ref = open("Student.txt", "r")
        for student in file_ref.readlines():
            add_student(student)
        file_ref.close()
    except Exception:
        print("Error reading file")


read_from_file()
print_students_names()

student_name = input("Enter student name")
student_id = input("Enter student id")

#add_student(student_name, student_id)
save_to_file(student_name)
"""

# Practice 2:


def read_from_file():
    try:
        file_ref = open("Student.txt", "r")
        for student in file_ref.readlines():
            add_student(student)
        file_ref.close()
    except Exception:
        print("Error reading file")

"""
read_from_file()
print_students_names()
"""


def save_to_file(student):
    try:
        file_ref = open("Student.txt", "a")
        file_ref.write(student +"\n")
        file_ref.close()
    except Exception:
        print("Error writing to the file")


stu_name = input("Enter student name")

print("reading from file before writing to it")
read_from_file()
print_students_names()

save_to_file(stu_name)

print("reading from file after writing to it")
read_from_file()
print_students_names()
students = []


def read_from_file():
    try:
        file_ref = open("Student.txt", "r")
        for student in read_students_generator(file_ref):
            students.append(student)
        file_ref.close()
    except Exception:
        print("Error reading file")


def read_students_generator(f):
    for student in f:
        yield student


read_from_file()
print(students)


# Practice 2:

def read_from_file():
    try:
        file_ref = open("Students.txt", "r")
        for student in read_file_generator(file_ref):
            students.append(student)
        file_ref.close()
    except Exception:
        print("Error reading file")


def read_file_generator(file_ref):
    for line in file_ref:
        yield line

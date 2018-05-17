students = []


def get_students_names():
    students_names = []
    for student in students:
        students_names.append(student)
    return students_names


def print_students_names():
    students_names = get_students_names()
    print(students_names)


def add_student(name, student_id=332):
    student = {"name" : name, "student_id" : student_id}
    students.append(student)


def var_args(name, *args):
    print(name)
    print(args)


def kwvar_args(name, **kwargs):
    print(name)
    print(kwargs)
    print(kwargs["lname"])


add_student("Joe")

add_student(("Mark", "989"))

print_students_names()

print("Hello", "World", True, 7)

var_args("Leo", 34, False, None, "Can")

kwvar_args(name="Amy", age=20, senior=False, lname="Rogers")
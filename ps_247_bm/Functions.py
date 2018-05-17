"""
students = ["Mark", "Adam", "Leo", "Zoe", "Han", "Nina"]

def get_students_names():
    students_names = []
    for student in students:
        students_names.append(student.title())
    return students_names


def print_students_names():
    students_names = get_students_names()
    print(students_names)


def add_student(name):
    students.append(name)


add_student("Karen")

print_students_names()
"""

# Practice 2
students = []


# def add_students(name, student_id=342): #default student_id if it isn't passed


def add_students(name, sid):
    students.append({"name":name, "id":sid})


def get_students():
    students_list = []
    for student in students:
        students_list.append(student)
    return students_list


def display_students():
    students_list = get_students()
    for student in students_list:
        print("Name:", student.get("name"))
        print("ID:", student["id"].title())


""" 
for index in range(5):
    student_name = input("Enter student name")
    student_id = input("Enter student id")
    add_students(student_name, student_id)
"""

# ask the user if he wants to add students

user_choice = input("Do you want to add a new student info?")
print(user_choice)

while user_choice == (' Y' or 'Y' or ' y' or 'y'):
        student_name = input("Enter student name")
        student_id = input("Enter student id")
        add_students(student_name, student_id)
        user_choice = input("Do you want to add a new student info?")
        print(user_choice)

display_students()


"""
def multiple_args(name, *args):
    print(name)
    print(args)


multiple_args("Andy", "Student", 23, True)



def multiple_kw_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


multiple_kw_args("Jamie", description="student", feedback="good", enrolled=True)

"""

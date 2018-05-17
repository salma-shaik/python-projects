students = []


def get_students():
    students_list = []
    for student in students:
        students_list.append(student)
    return students_list


def print_students():
    students_list = get_students()
    print(students_list)


def add_student(name, stud_id):
    student = dict(name=name, id=stud_id)
    students.append(student)


def accept_student_info():
    student_name = input("Enter a name")
    student_id = input("Enter an id")
    add_student(student_name, student_id)


initial_user_choice = True

while initial_user_choice:
    user_choice = input("Do you want to add a student? Please enter y for Yes and n for No")
    if user_choice == 'y':
        accept_student_info()
    else:
        initial_user_choice = False

if students:
    print_students()
else:
    print("No students added")

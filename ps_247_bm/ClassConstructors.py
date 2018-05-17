students = []

"""
class Student():
    def __init__(self, name, student_id=332):
        student = {
            "name": name,
            "student_id": student_id
        }
        students.append(student)

    def __str__(self):
        return "Student"


student = Student("Mark")
print(students)
print(student)
"""


# Practice 2
class Students:
    def __init__(self, name, student_id=32):
        student = {"name": name, "id": student_id}
        students.append(student)

    def __str__(self):
        return "Student"


student1 = Students("Mark")

print(students)
print(student1)


students = []

"""
class Student:
    def add_students(self, name, student_id=332):
        student = {"name":name, "student_id":student_id}
        students.append(student)


student = Student()
student.add_students("Mark")

print(students)
"""

# Practice 2
students = []


class Student():
    def add_student(self, name, student_id = "433"):
        student = {"name": name, "id": student_id}
        students.append(name)


student1 = Student()
student1.add_student("Jamie", 134)

print(students)


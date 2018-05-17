students = []

"""
class Student:

    school_name = "Little Tots"

    def __init__(self, name, student_id=45):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


student = Student("joe")

capital_name = student.get_name_capitalized()

print(capital_name)
# print(students)

#print(student)

#print(student.get_name_capitalized())

#print(Student.school_name)

"""
# Practice 2


class Students:
    school_name = "St.Marys"

    def __init__(self, name, student_id=23):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return "Student: " +self.name

    def get_school_name(self):
        return self.school_name

student1 = Students("Mark")

print(student1)

print(student1.get_school_name())


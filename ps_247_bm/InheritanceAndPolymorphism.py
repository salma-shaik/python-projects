students = []


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

#print(student)

capital_name = student.get_name_capitalized()
#print(capital_name)


"""
class HighSchoolStudent(Student):

    school_name = "Little Tots High School"

    def __init__(self, name):
        self.name = name

    def get_school_name(self):
        return HighSchoolStudent.school_name

    def get_name_capitalized(self):
        return super().get_name_capitalized()


student_hs = HighSchoolStudent("amy")

print(student_hs.name)

print(student_hs.get_name_capitalized())

"""


# Practice 2


class HighSchoolStudent(Student):
    def __str__(self):
        return "High School Student"

    def get_school_name(self):
        return "Loyola High School"

    def get_name_capitalized(self):
        return super().get_name_capitalized()+" ROB"


def student_details():
    hsStudent = HighSchoolStudent("mike")

    #print(hsStudent.name)

    #print(hsStudent)

    print(hsStudent.get_school_name())

    print(hsStudent.get_name_capitalized())


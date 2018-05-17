student_names = ["James", "Katarina", "Jessica"]

student_names[0] = "Mark"

#student_names[3] = "Homer" #list assignment index out of range

student_names.append("Homer")

print(student_names)

print("Mark" in student_names)

print("James" in student_names)

print(len(student_names))

print(len(student_names[2]))

del student_names[2]

print(student_names[2])

print(len(student_names[2]))

#negative indexes starting from -1 to get the items from the rear end of the list
print(student_names[-1])

#List slicing - these operations don't modify the lists. Just ignores some elements temporariliy
print(student_names[1:]) #ignoring the first element,Mark

print(student_names[:-1]) #ignoring the last element, Homer

print(student_names[1:-1]) #ignoring first(Mark) and last(Homer) elements


#Practice 2
students_list = ["Mark", "Jacob", "Katrina"]
#print(students_list)

students_list[1] = "Rachel"
print(students_list)

print(students_list[-2])

students_list.append("Alice")

print(students_list)

print("Mark" in students_list)
print("Adam" in students_list)

print(len(students_list))
print(len("Jonas"))

del students_list[2]

print(students_list)

print(students_list[1:])

print(students_list[1:-1])


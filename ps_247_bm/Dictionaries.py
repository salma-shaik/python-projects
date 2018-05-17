student = {"name": "Mark", "student_id": 6776}

print(student["name"])

print(student.get("last_name", "unknown"))

print(student.keys())

print(student.values())

student["name"]="James"

print(student["name"])

del student["name"]

print(student)


# Practice 2

student_details = {"id": 111, "name": "John", "feedback": None}
print(student_details)

# List of dictionaries
students_list = [
    {"id": 2, "name": "Amy"},
    {"id": 4, "name": "Rose"},
    {"id": 10, "name": "Emily"}
]

print(students_list)

# Iterate through list of dictionaries

for student in students_list:
    print(student.get("id"))
    print(student.get("name"))


print(student_details.keys())
print(student_details.values())


print(student_details["id"])

print(student_details.get("salary", "Unknown"))

print(student_details.get("salary")) # defaults to None since 2nd argument is not provided.

#print(student_details["salary"]) --> Key Error


student_details["name"] = "Jake"
print(student_details)

del student_details["feedback"]
print(student_details)



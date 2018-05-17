student = {"name": "Mark", "student_id": 6466, "last_name": "Zucker"}

"""
try:
    last_name = student["last_name"]
    # numbered_last_name = 3 + last_name
    print(3/0)
    # print(last_name)
except KeyError:
    print("Error finding last_name")
except TypeError:
    print("int and str can't be added together")
except Exception:
    print("Unknown error")
print("This code executes!")
"""


# Practice 2:

try:
    student["first_name"] = "Mary"
    print(student["first_name"])

    print(student["first_name"] + 4)

    print(4 + student["first_name"])

except KeyError:
    print("first_name is not defined")

except TypeError as error:
    print("Cannot add str and int together")
    print("Error cause: ", error)

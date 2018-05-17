number = 0

if not number:
    print("Zero")
else:
    print(number)

text = ""
if text:
    print("not empty")
else:
    print("empty string")


# Practice 2
python_course = True
java_course = True
sql_course = False
aliens_found = None #assumes '0' or False value by default

if python_course:
    print("It's a python course")
else:
    print("It's not a python course")

if aliens_found:
    print("This will not be printed")

if python_course and java_course:
    print("2 programming language courses")

if python_course and sql_course:
    print("programming and db")

if java_course or sql_course:
    print("at least 1 course")

a = 1
b = 2

comparison_result = "bigger" if a>b else "smaller"
#print(comparison_result)

print("bigger" if a>b else "smaller")
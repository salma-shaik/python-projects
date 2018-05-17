id = 5
net_salary = 468.75
taxes = 200
total_salary = net_salary+taxes
first_name = "Joe"
last_name = 'Roy'
"""
    This is 
    a multiline
    comment
"""
#This is a single line comment
comment = """Hello"""
#print(comment)
#print("Employee name is")

print("hello".capitalize())
print("hello".replace('h','j'))
print("hello".isalpha())
print("123".isdigit())
print("this, is, split".split(','))

print("Employee first name is {0} and last name is {1}".format(first_name, last_name))

print(f"Employee salary is {total_salary} and taxes are {taxes}")


python_course = True
java_course = False

print(python_course)
print(java_course)

print(int(python_course))
print(int(java_course))

aliens_found = None
print(aliens_found)
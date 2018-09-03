student = {'name':'John', 'age': 25, 'courses':['math' ,'art' ,'history']}
print(student)

print(student['name'])

print(student['name'] == 'John')

print(student['courses'])

#print(student['phone'])

print(student.get('name'))

print(student.get('phone', 'Not Found'))

student['phone'] = '3423434'

print(student)

student['name'] = 'James'

print(student)

student.update({'name' : 'Jane', 'age': 26, 'phone':'2343243'})

print(student)

del student['age']

print(student)

print(student.pop('phone'))

print(student)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key, value in student.items():
    print("key:{}, value:{} ".format(key, value))



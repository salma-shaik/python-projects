'''
Regular tuple but more readable
'''

from collections import namedtuple

# list/tuple
color = (55, 155, 255)
# print(color[0])

# dict
color = {'red': 55, 'green': 155, 'blue': 255}
# print(color['red'])

#named tuple
employee_info = namedtuple('employee', ['id', 'title', 'salary'])
emp1 = employee_info('John', 'Manager', '100000')
emp2 = employee_info('Mary', 'HR', '90000')

print(emp1.id)
print(emp2.title)

print(emp2)

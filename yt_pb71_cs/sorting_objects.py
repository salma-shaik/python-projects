from operator import attrgetter

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


'''
def emp_sort_name(emp):
    return emp.name
'''


def emp_sort_age(emp):
    return emp.age


def emp_sort_salary(emp):
    return emp.salary


emp1 = Employee('Sara', 35, 58000)
emp2 = Employee('Jake', 23, 32320)
emp3 = Employee('Amy', 32, 90000)

employees = [emp1, emp2, emp3]
# s_employees = sorted(employees, key=emp_sort_name)
# s_employees = sorted(employees, key=emp_sort_age)
# s_employees = sorted(employees, key=emp_sort_salary, reverse=True)

# print(s_employees)

lambda_s_employees = sorted(employees, key=lambda e: e.name, reverse=True)
print('Using lambda: ', lambda_s_employees)

attrgetter_s_employees = sorted(employees, key=attrgetter('age'), reverse=True)
print(attrgetter_s_employees)

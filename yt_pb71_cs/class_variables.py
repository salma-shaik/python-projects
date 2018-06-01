class Employee:
    # receives the instance as the 1st arg automatically
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount


print(Employee.num_of_emps)

emp1 = Employee('James', 'Smith', '50000')
emp2 = Employee('Test', 'User', '60000')

print(Employee.num_of_emps)
# emp1.apply_raise()
# emp2.apply_raise()
#
# print(emp1.pay)
# print(emp2.pay)

# Employee.raise_amount = 1.05

# when we are assigning here, raise_amount is created within the namespace of emp1
# emp1.raise_amount = 1.05
#
# emp1.apply_raise()
# emp2.apply_raise()
#
# print(emp1.pay)
# print(emp2.pay)
#
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)
#
# print(emp1.__dict__)
# print(Employee.__dict__)




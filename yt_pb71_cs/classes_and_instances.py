class Employee:
    # receives the instance as the 1st arg automatically
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'


emp1 = Employee('James', 'Smith', '50000')
emp2 = Employee('Test', 'User', '60000')

# print(emp1)
# print(emp2)

print(emp1.email)
print(emp2.email)

# print(f'{emp1.first} {emp1.last}')
print(emp1.full_name()) # --> gets transformed to Employee.full_name(emp1)
print(emp2.full_name())

# when callin directly with the class, need to explicitly pass self instance
print(Employee.full_name(emp1))

"""
emp1.first = 'James'
emp1.last = 'Smith'
emp1.email = 'James.Smith@company.com'
emp1.pay = 50000

emp2.first = 'test'
emp2.last = 'user'
emp2.email = 'test.user@company.com'
emp2.pay = 60000

print(emp1.email)
print(emp2.email)
"""
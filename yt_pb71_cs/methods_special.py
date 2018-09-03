class Employee:
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

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp1 = Employee('James', 'Smith', 50000)
emp2 = Employee('Test', 'User', 60000)

print("just emp1: ", emp1)

print('str(emp1): ', str(emp1))
print('repr(emp1): ', repr(emp1))

print(emp1.__str__())
print(emp1.__repr__())
#
# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a','b'))
# print(str.__add__('1','2'))
#
print(emp1 + emp2)
#
# print(len('test'))
# print('test'.__len__())
#
# print(emp1.__len__())
# print(len(emp2))

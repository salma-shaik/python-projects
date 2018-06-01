class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first+'.'+last+'@company.com'
        Employee.num_of_emps += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Delete name')
        self.first = None
        self.last = None


emp1 = Employee('James', 'Smith', 50000)
print(emp1.first)
print(emp1.email)
print(emp1.full_name)

emp1.first = 'Mary'
print(emp1.first)
print(emp1.email)
print(emp1.full_name)

emp1.full_name = 'Jason Smith'
print(emp1.first)
print(emp1.email)
print(emp1.full_name)

del emp1.full_name
print(emp1.first)
print(emp1.email)
print(emp1.full_name)

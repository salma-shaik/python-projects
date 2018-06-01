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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        print(len(self.employees))
        for emp in self.employees:
            print('--> ', emp.full_name())


# Creating employee objects
# dev1 = Employee('James', 'Smith', '50000')
# dev2 = Employee('Test', 'User', '60000')
#
# print(dev1.email)
# print(dev1.email)


# Creating developer objects
dev1 = Developer('James', 'Smith', '50000', 'Python')
dev2 = Developer('Test', 'User', '60000', 'Java')

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

# print(help(Developer))

# print(dev1.email)
# print(dev1.prog_lang)
# print(dev2.email)
# print(dev2.prog_lang)

# Create manager objects
mgr1 = Manager('Sue', 'Bran', '100000', [dev1])
mgr1.add_emp(dev2)

# print(mgr1.email)
mgr1.print_emp()

# mgr1.rem_emp(dev1)
# print(mgr1.print_emp())

print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))

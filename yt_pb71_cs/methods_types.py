# regular methods in a class automatically takes an instance as the 1st arg
# class method - automatically pass class as the 1st arg - cls
# static methods - don't pass anything automatically


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

    def test_method(self, msg):
        print(msg)


emp1 = Employee('James', 'Smith', '50000')
print(emp1.test_method("Hi"))
# emp2 = Employee('Test', 'User', '60000')
#
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)

# Employee.set_raise_amt(1.05)
# emp1.set_raise_amt(1.05) # --> Not recommended
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)


# emp_str1 = 'Jon-Doe-150000'
# emp_str1 = 'Ann-Mary-750000'
#
# first, last, pay = emp_str1.split('-')
# emp1 = Employee(first, last, pay)
#
# print(emp1.full_name())

# emp1 = Employee.from_string('Jon-Doe-150000')
# print(emp1.full_name())
# print(emp1.pay)

import datetime
date1 = datetime.date(2018, 5, 27)

print(Employee.is_workday(date1))


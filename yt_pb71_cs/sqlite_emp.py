class Employee:
    """ A sample employee class"""
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first+'.'+last+'@company.com'

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return "Employee ('{}', '{}', '{}').format(self.first, self.last, self.pay)"


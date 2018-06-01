import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler= logging.FileHandler('logging_emp_class.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename='logging_emp_class.log', level=logging.INFO,
#                     format='%(levelname)s:%(name)s:%(message)s')


class Employee:
    """ A sample employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee: {self.full_name} - {self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'


emp1 = Employee('James', 'Smith')
emp2 = Employee('Jane', 'Doe')
emp3 = Employee('Mary', 'Rogers')

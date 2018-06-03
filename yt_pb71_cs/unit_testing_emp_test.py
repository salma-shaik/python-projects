import unittest
from unit_testing_emp import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp1 = Employee('John', 'Smith', 50000)
        self.emp2 = Employee('Sue', 'Rogers', 60000)
    
    def tearDown(self):
        print('tearDown')
        pass
        
    def test_email(self):
        print('test_email')
        # self.emp1 = Employee('John', 'Smith', 50000)
        # self.emp2 = Employee('Sue', 'Rogers', 60000)

        self.assertEqual(self.emp1.email, 'John.Smith@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Rogers@email.com')

        self.emp1.first = 'Jane'
        self.emp2.first = 'Amy'

        self.assertEqual(self.emp1.email, 'Jane.Smith@email.com')
        self.assertEqual(self.emp2.email, 'Amy.Rogers@email.com')

    def test_full_name(self):
        print('test_full_name')
        # self.emp1 = Employee('John', 'Smith', 50000)
        # self.emp2 = Employee('Sue', 'Rogers', 60000)

        self.assertEqual(self.emp1.full_name, 'John Smith')
        self.assertEqual(self.emp2.full_name, 'Sue Rogers')

        self.emp1.first = 'Zack'
        self.emp2.first = 'Sara'

        self.assertEqual(self.emp1.full_name, 'Zack Smith')
        self.assertEqual(self.emp2.full_name, 'Sara Rogers')

    def test_apply_raise(self):
        print('test_apply_raise')
        # self.emp1 = Employee('John', 'Smith', 50000)
        # self.emp2 = Employee('Sue', 'Rogers', 60000)

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52000)
        self.assertEqual(self.emp2.pay, 62400)

    # Mocking
    def test_monthly_schedule(self):
        with patch('unit_testing_emp.requests.get') as mocked_get:

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')

            # mocked_get.return_value.ok = False
            # schedule = self.emp2.monthly_schedule('June')
            # mocked_get.assert_called_with('http://company.com/Rogers/June')
            #
            # self.assertEqual(schedule, 'Bad Response')


if __name__ == '__main__':
    unittest.main()

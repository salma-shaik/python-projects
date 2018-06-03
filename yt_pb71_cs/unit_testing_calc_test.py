import unittest
import unit_testing_calc


class TestCalc(unittest.TestCase):

    def test_add(self):
    # def add_test(self):
        # result = unit_testing_calc.add(10, 5)
        self.assertEqual(unit_testing_calc.add(10, 5), 15)
        self.assertEqual(unit_testing_calc.add(-1, 1), 0)
        self.assertEqual(unit_testing_calc.add(-1, -1), -2)

        # self.assertEqual(result, 14)

    def test_sub(self):
        self.assertEqual(unit_testing_calc.subtract(10, 5), 5)
        self.assertEqual(unit_testing_calc.subtract(-1, 1), -2)
        self.assertEqual(unit_testing_calc.subtract(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(unit_testing_calc.multiply(10, 5), 50)
        self.assertEqual(unit_testing_calc.multiply(-1, 1), -1)
        self.assertEqual(unit_testing_calc.multiply(-1, -1), 1)

    def test_div(self):
        self.assertEqual(unit_testing_calc.divide(10, 5), 2)
        self.assertEqual(unit_testing_calc.divide(-1, 1), -1)
        self.assertEqual(unit_testing_calc.divide(-1, -1), 1)
        self.assertEqual(unit_testing_calc.divide(5, 2), 2.5)

       # self.assertRaises(ValueError, unit_testing_calc.divide, 10, 2)
       # self.assertRaises(ValueError, unit_testing_calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            unit_testing_calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
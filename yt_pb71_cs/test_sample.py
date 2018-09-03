import unittest
import sample


class TestSample(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sample.add(10, 5), 15)
        self.assertEqual(sample.add(-1, 1), 0)
        self.assertEqual(sample.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(sample.subtract(10, 5), 5)
        self.assertEqual(sample.subtract(-1, 1), -2)
        self.assertEqual(sample.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(sample.multiply(10, 5), 50)
        self.assertEqual(sample.multiply(-1, 1), -1)
        self.assertEqual(sample.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(sample.divide(10, 5), 2)
        self.assertEqual(sample.divide(-1, 1), -1)
        self.assertEqual(sample.divide(-1, -1), 1)
        self.assertEqual(sample.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            sample.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
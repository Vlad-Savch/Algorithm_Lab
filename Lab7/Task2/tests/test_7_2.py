import unittest
from Lab7.Task2.src.task_calculator import primitive_calculator


class TestPrimitiveCalculator(unittest.TestCase):
    def test_case_1(self):
        n = 1
        operations, sequence = primitive_calculator(n)
        self.assertEqual(operations, 0)
        self.assertEqual(sequence, [1])

    def test_case_5(self):
        n = 5
        operations, sequence = primitive_calculator(n)
        self.assertEqual(operations, 3)
        self.assertEqual(sequence, [1, 3, 4, 5])

    def test_case_10(self):
        n = 10
        operations, sequence = primitive_calculator(n)
        self.assertEqual(operations, 3)
        self.assertIn(sequence, [[1, 3, 9, 10], [1, 2, 4, 5, 10]])


if __name__ == '__main__':
    unittest.main()

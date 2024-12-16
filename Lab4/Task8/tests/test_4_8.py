import unittest
from Lab4.Task8.src.task_postfix import postfix


class TestPostfix(unittest.TestCase):
    def test_task_case(self):
        expression = ["8", "9", "+", "1", "7", "-", "*"]

        result = postfix(expression)
        expected = -102

        self.assertEqual(result, expected)

    def test_single_number(self):
        expression = ["5"]

        result = postfix(expression)
        expected = 5

        self.assertEqual(result, expected)

    def test_multiple_operations(self):
        expression = ["3", "4", "+", "2", "*", "7", "+"]

        result = postfix(expression)
        expected = 21

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

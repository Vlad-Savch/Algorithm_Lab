import unittest

from Lab6.Task6.src.task_is_fibonacci import process_queries


class TestFibonacciNumbers(unittest.TestCase):

    def test_case_1(self):
        queries = ["1", "2", "3", "4", "5", "6", "7", "8"]
        expected_output = ["Yes", "Yes", "Yes", "No", "Yes", "No", "No", "Yes"]

        result = process_queries(queries)

        self.assertEqual(result, expected_output)

    def test_case_2(self):
        queries = ["13", "21", "34", "55", "89", "144"]
        expected_output = ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]

        result = process_queries(queries)

        self.assertEqual(result, expected_output)

    def test_case_3(self):
        queries = ["100", "200", "300", "400", "500"]
        expected_output = ["No", "No", "No", "No", "No"]

        result = process_queries(queries)

        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()

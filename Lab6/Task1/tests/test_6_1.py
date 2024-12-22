import unittest
from Lab6.Task1.src.task_set_operations import process_operations


class TestOperations(unittest.TestCase):

    def test_case_1(self):
        input_data =[('A', 2),
                     ('A', 5),
                     ('A', 3),
                     ('?', 2),
                     ('?', 4),
                     ('A', 2),
                     ('D', 2),
                     ('?', 2)]
        expected_output = ['Y', 'N', 'N']

        result = process_operations(input_data)

        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input_data = [('A', 10),
                      ('?', 10),
                      ('D', 10),
                      ('?', 10)]
        expected_output = ['Y', 'N']

        result = process_operations(input_data)

        self.assertEqual(result, expected_output)

    def test_case_3(self):
        input_data = [('?', 1),
                      ('A', 1),
                      ('?', 1)]
        expected_output = ['N', 'Y']

        result = process_operations(input_data)

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

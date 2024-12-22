import unittest
from Lab6.Task4.src.task_associative_array import process_operations


class TestAssociativeArray(unittest.TestCase):

    def test_case_1(self):
        operations = [
            "put zero a",
            "put one b",
            "put two c",
            "put three d",
            "put four e",
            "get two",
            "prev two",
            "next two",
            "delete one",
            "delete three",
            "get two",
            "prev two",
            "next two",
            "next four"
        ]
        expected_output = [
            "c",
            "b",
            "d",
            "c",
            "a",
            "e",
            "<none>"
        ]

        result = process_operations(operations)

        self.assertEqual(result, expected_output)

    def test_case_2(self):
        operations = [
            "put zero a",
            "get zero",
            "prev zero",
            "next zero",
            "put zero b",
            "get zero",
            "delete zero",
            "get zero"
        ]
        expected_output = [
            "a",
            "<none>",
            "<none>",
            "b",
            "<none>"
        ]

        result = process_operations(operations)

        self.assertEqual(result, expected_output)

    def test_case_3(self):
        operations = [
            "put one x",
            "put two y",
            "put three z",
            "prev two",
            "next two",
            "delete two",
            "get two",
            "prev two",
            "next two"
        ]
        expected_output = [
            "x",
            "z",
            "<none>",
            "<none>",
            "<none>"
        ]

        result = process_operations(operations)

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

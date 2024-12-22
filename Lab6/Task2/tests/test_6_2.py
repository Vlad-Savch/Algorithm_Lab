import unittest
from Lab6.Task2.src.task_phonebook import process_queries


class TestPhonebook(unittest.TestCase):

    def test_case_1(self):
        queries = [
            "add 911 police",
            "add 76213 Mom",
            "add 17239 Bob",
            "find 76213",
            "find 910",
            "find 911",
            "del 910",
            "del 911",
            "find 911",
            "find 76213",
            "add 76213 daddy",
            "find 76213"
        ]
        expected_output = [
            "Mom",
            "not found",
            "police",
            "not found",
            "Mom",
            "daddy"
        ]

        result = process_queries(queries)

        self.assertEqual(result, expected_output)

    def test_case_2(self):
        queries = [
            "add 12345 Alice",
            "find 12345",
            "del 12345"
        ]
        expected_output = [
            "Alice"
        ]

        result = process_queries(queries)

        self.assertEqual(result, expected_output)

    def test_case_3(self):
        queries = [
            "add 555123 John",
            "find 555123",
            "add 555123 Mike",
            "find 555123",
            "del 555123"
        ]
        expected_output = [
            "John",
            "Mike"
        ]

        result = process_queries(queries)

        self.assertEqual(result, expected_output)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()

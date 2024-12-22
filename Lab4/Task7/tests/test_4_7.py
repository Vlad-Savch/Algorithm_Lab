import unittest
from Lab4.Task7.src.task_max_in_sequence import max_in_sequence


class TestMaxInSequence(unittest.TestCase):
    def test_task(self):
        n = 8
        arr = [2, 7, 3, 1, 5, 2, 6, 2]
        m = 4

        result = max_in_sequence(n, arr, m)
        expected = [7, 7, 5, 6, 6]

        self.assertEqual(result, expected)

    def test_window(self):
        n = 5
        arr = [1, 3, -1, -3, 5]
        m = 3

        result = max_in_sequence(n, arr, m)
        expected = [3, 3, 5]

        self.assertEqual(result, expected)

    def test_full_window(self):
        n = 4
        arr = [1, 2, 3, 4]
        m = 4

        result = max_in_sequence(n, arr, m)
        expected = [4]

        self.assertEqual(result, expected)

    def test_single_element(self):
        n = 1
        arr = [10]
        m = 1

        result = max_in_sequence(n, arr, m)
        expected = [10]

        self.assertEqual(result, expected)

    def test_same_elements(self):
        n = 3
        arr = [4, 4, 4]
        m = 2

        result = max_in_sequence(n, arr, m)
        expected = [4, 4]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

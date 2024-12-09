import unittest
from Lab3.Task3.src.task_scarecrow import scarecrow_sort


class TestScarecrowSort(unittest.TestCase):
    def test_case_1(self):
        n = 3
        k = 2
        dolls = [2, 1, 3]
        result = scarecrow_sort(n, k, dolls)
        self.assertEqual(result, "НЕТ")

    def test_case_2(self):
        n = 5
        k = 3
        dolls = [1, 5, 3, 4, 1]
        result = scarecrow_sort(n, k, dolls)
        self.assertEqual(result, "ДА")

    def test_case_3(self):
        n = 4
        k = 1
        dolls = [4, 3, 2, 1]
        result = scarecrow_sort(n, k, dolls)
        self.assertEqual(result, "ДА")

    def test_case_4(self):
        n = 6
        k = 3
        dolls = [1, 2, 3, 4, 5, 6]
        result = scarecrow_sort(n, k, dolls)
        self.assertEqual(result, "ДА")

    def test_case_5(self):
        n = 5
        k = 3
        dolls = [7, 7, 7, 7, 7]
        result = scarecrow_sort(n, k, dolls)
        self.assertEqual(result, "ДА")


if __name__ == '__main__':
    unittest.main()

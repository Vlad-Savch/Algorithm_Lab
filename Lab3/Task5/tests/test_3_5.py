import unittest
from Lab3.Task5.src.task_h_index import hirsch_index


class TestHirschIndex(unittest.TestCase):
    def test_case_1(self):
        citations = [3, 0, 6, 1, 5]
        self.assertEqual(hirsch_index(citations), 3)

    def test_case_2(self):
        citations = [1, 3, 1]
        self.assertEqual(hirsch_index(citations), 1)

    def test_case_4(self):
        citations = [10, 8, 5, 4, 3]
        self.assertEqual(hirsch_index(citations), 4)

    def test_case_5(self):
        citations = [25, 8, 5, 3, 3]
        self.assertEqual(hirsch_index(citations), 3)


if __name__ == "__main__":
    unittest.main()

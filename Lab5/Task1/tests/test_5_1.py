import unittest
from Lab5.Task1.src.task_is_heap import is_heap


class TestIsHeap(unittest.TestCase):

    def test_heap_1(self):

        n = 5
        arr = [1, 3, 2, 5, 4]

        result = is_heap(n, arr)

        self.assertEqual(result, "YES")

    def test_heap_2(self):
        n = 5
        arr = [5, 0, 1, 2, 0]

        result = is_heap(n, arr)

        self.assertEqual(result, "NO")

    def test_single_element(self):
        n = 1
        arr = [10]

        result = is_heap(n, arr)

        self.assertEqual(result, "YES")

    def test_all_elements_are_equal(self):
        n = 4
        arr = [5, 5, 5, 5]

        result = is_heap(n, arr)

        self.assertEqual(result, "YES")

    def test_no_left_child(self):
        n = 3
        arr = [1, 2, 3]

        result = is_heap(n, arr)

        self.assertEqual(result, "YES")

    def test_not_a_heap(self):
        n = 6
        arr = [10, 5, 20, 3, 30, 15]

        result = is_heap(n, arr)

        self.assertEqual(result, "NO")

    def test_large_heap(self):
        n = 1000
        arr = [i for i in range(1, n+1)]

        result = is_heap(n, arr)

        self.assertEqual(result, "YES")


if __name__ == "__main__":
    unittest.main()

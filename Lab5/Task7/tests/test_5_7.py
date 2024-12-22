import unittest
from Lab5.Task7.src.task_heap_reversed import heap_sort


class TestHeapSort(unittest.TestCase):
    def test_example(self):
        arr = [10, 5, 6, 2, 8, 1, 4, 9, 3, 7]

        result = heap_sort(arr)

        self.assertEqual(result, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_single_element(self):
        arr = [10]

        result = heap_sort(arr)

        self.assertEqual(result, [10])

    def test_sorted_reversed_array(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        result = heap_sort(arr)

        self.assertEqual(result, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        result = heap_sort(arr)

        self.assertEqual(result, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()

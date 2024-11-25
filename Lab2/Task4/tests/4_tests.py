import unittest
from Lab2.Task4.src.four import binary_search, main
from utils import time_data, memory_data


class TestMainFunction(unittest.TestCase):
    def setUp(self):
        self.expected_output = "2 0 -1 0 -1"

        self.input_file = "../../Task4/txtf/input.txt"
        self.output_file = "../../Task4/txtf/output.txt"

    def test_main(self):
        main()

        with open(self.output_file, "r") as f:
            output = f.read()
            self.assertEqual(output, self.expected_output)

    def test_binary_search(self):
        with open(self.input_file, "r") as f:
            data = f.readlines()
            a = list(map(int, data[1].split()))
            b = list(map(int, data[3].split()))

            expected_result = [binary_search(a, x) for x in b]

            self.assertEqual(expected_result, [2, 0, -1, 0, -1])

    def test_time_memory_data(self):
        print('Время работы: ', time_data(main), ' секунд')
        print('Память: ', memory_data(main), 'Мб')

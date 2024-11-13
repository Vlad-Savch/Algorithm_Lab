import unittest
import os
from Lab2.four import binary_search, main


class TestMainFunction(unittest.TestCase):
    def setUp(self):
        self.input_data = "5\n1 5 8 12 13\n5\n8 1 23 1 11"
        self.expected_output = "2 0 -1 0 -1"

        self.input_file = "input.txt"
        self.output_file = "output.txt"

        with open(self.input_file, "w") as f:
            f.write(self.input_data)

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

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

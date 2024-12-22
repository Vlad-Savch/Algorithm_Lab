import os
from utils import read_array_from_file, write_array_to_file


def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def process_file(input_path, output_path):
    with open(input_path, 'r') as file:
        n = int(file.readline().strip())
        a = list(map(int, file.readline().split()))
        k = int(file.readline().strip())
        b = list(map(int, file.readline().split()))

    result = [binary_search(a, x) for x in b]

    write_array_to_file(output_path, result)


def main():
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, '../../Task4/txtf/input.txt')
    output_path = os.path.join(base_dir, '../../Task4/txtf/output.txt')

    process_file(input_path, output_path)


if __name__ == "__main__":
    main()

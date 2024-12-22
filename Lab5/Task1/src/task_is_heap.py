import os
from utils import write_string_to_file, read_array_from_file


def is_heap(n, arr):
    for i in range(1, n + 1):
        left = 2 * i
        right = 2 * i + 1

        if left <= n and arr[i - 1] > arr[left - 1]:
            return "NO"

        if right <= n and arr[i - 1] > arr[right - 1]:
            return "NO"

    return "YES"


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    result = is_heap(n, arr)

    write_string_to_file(output_path, result)


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

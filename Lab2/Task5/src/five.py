import os
from utils import read_array_from_file, write_array_to_file


def majority_element(a, left, right):
    if left == right:
        return a[left]

    mid = (left + right) // 2
    left_candidate = majority_element(a, left, mid)
    right_candidate = majority_element(a, mid + 1, right)

    if left_candidate == right_candidate:
        return left_candidate

    left_count = sum(1 for i in range(left, right + 1) if a[i] == left_candidate)
    right_count = sum(1 for i in range(left, right + 1) if a[i] == right_candidate)

    if left_count > (right - left + 1) // 2:
        return left_candidate
    if right_count > (right - left + 1) // 2:
        return right_candidate

    return None


def solve(a):
    n = len(a)
    candidate = majority_element(a, 0, n - 1)

    if candidate is None:
        return 0

    count = sum(1 for x in a if x == candidate)
    if count > n // 2:
        return 1
    else:
        return 0


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    array = read_array_from_file(input_filename)
    result = solve(array)
    write_array_to_file(output_filename, str(result))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

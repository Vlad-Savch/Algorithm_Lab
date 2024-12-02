from utils import read_array_from_file, write_array_to_file
import os

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def sort_file(input_filename="input.txt", output_filename="output.txt"):
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    array = read_array_from_file(input_filename)
    sorted_array = merge_sort(array)
    write_array_to_file(output_filename, sorted_array)


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    sort_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

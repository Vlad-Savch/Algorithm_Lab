import os
from utils import read_array_from_file, write_array_to_file


def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    while True:
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            i = smallest
            left = 2 * i + 1
            right = 2 * i + 2
        else:
            break


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)

    return arr


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    arr = read_array_from_file(input_path)

    sorted_arr = heap_sort(arr)

    write_array_to_file(output_path, sorted_arr)


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

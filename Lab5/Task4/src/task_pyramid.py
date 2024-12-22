import os
from utils import read_array_from_file, write_array_to_file


def build_min_heap(arr):
    n = len(arr)
    swaps = []

    def sift_down(i):
        """Функция просеивания вниз."""
        min_index = i
        left = 2 * i + 1
        if left < n and arr[left] < arr[min_index]:
            min_index = left

        right = 2 * i + 2
        if right < n and arr[right] < arr[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))
            arr[i], arr[min_index] = arr[min_index], arr[i]
            sift_down(min_index)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    arr = read_array_from_file(input_path)

    swaps = build_min_heap(arr)

    with open(output_path, "w") as file:
        file.write(str(len(swaps)) + "\n")
        for i, j in swaps:
            file.write(f"{i} {j}\n")


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

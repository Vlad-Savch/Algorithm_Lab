from utils import read_array_from_file, write_array_to_file
import os

def merge_count(arr, temp_arr, left, right):
    if left == right:
        return 0

    mid = (left + right) // 2
    inv_count = 0

    inv_count += merge_count(arr, temp_arr, left, mid)
    inv_count += merge_count(arr, temp_arr, mid + 1, right)

    inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def count_inversions(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_count(arr, temp_arr, 0, n - 1)


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    array, n = read_array_from_file(input_path)
    result = count_inversions(array)
    write_array_to_file(output_path, str(result))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

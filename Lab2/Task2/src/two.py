import os
from utils import read_array_from_file


def merge(arr, left, mid, right, output_file):
    temp = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]

    output_file.write(f"{left + 1} {right + 1} {arr[left]} {arr[right]}\n")


def merge_sort(arr, left, right, output_file):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, output_file)
        merge_sort(arr, mid + 1, right, output_file)
        merge(arr, left, mid, right, output_file)
    return arr


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    array = read_array_from_file(input_path)
    with open(output_path, 'w') as output_file:
        merge_sort(array, 0, len(array) - 1, output_file)
        output_file.write(" ".join(map(str, array)))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()


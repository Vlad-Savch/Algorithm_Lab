import random
from utils import read_array_from_file, write_array_to_file


def partition3(arr, low, high):
    pivot = arr[high]
    i = low
    lt = low
    gt = high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt


def randomized_partition3(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition3(arr, low, high)


def randomized_quick_sort3(arr, low, high):
    if low < high:
        lt, gt = randomized_partition3(arr, low, high)
        randomized_quick_sort3(arr, low, lt - 1)
        randomized_quick_sort3(arr, gt + 1, high)


def quick_sort_file3(input_filename, output_filename):
    arr = read_array_from_file(input_filename)
    randomized_quick_sort3(arr, 0, len(arr) - 1)
    write_array_to_file(output_filename, arr)


def main():
    quick_sort_file3('../txtf/input.txt', '../txtf/output.txt')


if __name__ == "__main__":
    main()
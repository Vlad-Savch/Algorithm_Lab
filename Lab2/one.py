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


def read_array_from_file(filename):
    with open(filename, "r") as f:
        f.readline()
        array = list(map(int, f.readline().strip().split()))
    return array


def write_array_to_file(filename, array):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, array)))


def sort_file(input_filename="input.txt", output_filename="output.txt"):
    array = read_array_from_file(input_filename)
    sorted_array = merge_sort(array)
    write_array_to_file(output_filename, sorted_array)


if __name__ == "__main__":
    sort_file("input.txt", "output.txt")

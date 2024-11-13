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


def read_array_from_file(filename):
    with open(filename, "r") as f:
        f.readline()
        array = list(map(int, f.readline().strip().split()))
    return array


def write_array_to_file(filename, array):
    with open(filename, "a") as f:
        f.write(" ".join(map(str, array)))


def sort_file(input_filename="input.txt", output_filename="output.txt"):
    arr = read_array_from_file(input_filename)

    with open(output_filename, "w") as output_file:
        merge_sort(arr, 0, len(arr) - 1, output_file)
    write_array_to_file(output_filename, arr)


if __name__ == "__main__":
    sort_file("input.txt", "output.txt")

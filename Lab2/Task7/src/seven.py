def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


def main():
    with open('../../Task7/txtf/input.txt', 'r') as file:
        n = int(file.readline())
        array = list(map(int, file.readline().split()))

    result = max_subarray_sum(array)

    with open('../../Task7/txtf/output.txt', 'w') as file:
        file.write(str(result))


if __name__ == '__main__':
    main()
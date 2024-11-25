def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    with open('../../Task4/txtf/input.txt', 'r') as file:
        n = int(file.readline().strip())
        a = list(map(int, file.readline().split()))
        k = int(file.readline().strip())
        b = list(map(int, file.readline().split()))

    result = [binary_search(a, x) for x in b]

    with open('../../Task4/txtf/output.txt', 'w') as file:
        file.write(' '.join(map(str, result)))


if __name__ == "__main__":
    main()

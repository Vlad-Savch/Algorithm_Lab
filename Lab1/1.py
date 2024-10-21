import time


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    t_start = time.perf_counter()
    insertion_sort(arr)
    print(time.perf_counter() - t_start, 'секунд')

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, arr)))


if __name__ == '__main__':
    main()

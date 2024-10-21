import time
t_start = time.perf_counter()

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            swap(arr, j, j + 1)
            j -= 1
        arr[j + 1] = key


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))

insertion_sort(arr)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, arr)))

print(time.perf_counter() - t_start, 'секунд')
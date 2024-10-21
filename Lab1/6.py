import time
t_start = time.perf_counter()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))

bubble_sort(arr)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, arr)))

print(time.perf_counter() - t_start, 'секунд')
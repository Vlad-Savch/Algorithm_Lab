import time
t_start = time.perf_counter()

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))

selection_sort(arr)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, arr)))

print(time.perf_counter() - t_start, 'секунд')
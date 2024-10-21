import time
t_start = time.perf_counter()

def linear_search(arr, v):
    for i in range(len(arr)):
        if arr[i] == v:
            return i
    return -1


with open('input.txt', 'r') as file:
    arr = file.readline().strip().split()
    v = file.readline().strip()

    if arr[0].isdigit():
        arr = list(map(int, arr))
        v = int(v)

result = linear_search(arr, v)

with open('output.txt', 'w') as file:
    file.write(str(result))

print(time.perf_counter() - t_start, 'секунд')
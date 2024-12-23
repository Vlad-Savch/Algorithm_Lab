from collections import deque
import os
from utils import print_time_memory_data


def max_in_sequence(n, arr, m):
    result = []
    dq = deque()

    for i in range(n):
        while dq and dq[0] < i - m + 1:
            dq.popleft()

        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        dq.append(i)

        if i >= m - 1:
            result.append(arr[dq[0]])

    return result


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
        m = int(file.readline())

    output = max_in_sequence(n, arr, m)

    with open(output_path, "w") as file:
        file.write(" ".join(map(str, output)))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
    print_time_memory_data(main)

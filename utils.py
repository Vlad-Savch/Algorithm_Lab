import time
import tracemalloc


def time_data(func):
    time_start = time.perf_counter()
    func()
    return time.perf_counter() - time_start


def memory_data(func):
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    return current / 1024 ** 2


def read_array_from_file(input_filename):
    with open(input_filename, "r") as f:
        n = int(f.readline().strip())
        array = list(map(int, f.readline().strip().split()))
    return array, n


def write_array_to_file(output_filename, array):
    with open(output_filename, "w") as f:
        f.write(' '.join(map(str, array)))


def write_string_to_file(output_filename, string):
    with open(output_filename, "w") as f:
        f.write(str(string))

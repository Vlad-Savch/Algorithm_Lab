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

import os
from utils import print_time_memory_data


def scarecrow_sort(n, k, dolls):
    buckets = {}

    for i in range(n):
        key = i % k
        if key not in buckets:
            buckets[key] = []
        buckets[key].append(dolls[i])

    for key in buckets:
        buckets[key].sort()

    sorted_dolls = []
    for i in range(n):
        key = i % k
        sorted_dolls.append(buckets[key].pop(0))

    for i in range(1, n):
        if sorted_dolls[i] < sorted_dolls[i - 1]:
            return "НЕТ"
    return "ДА"


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r", encoding="utf-8") as infile:
        n, k = map(int, infile.readline().split())
        dolls = list(map(int, infile.readline().split()))

    result = scarecrow_sort(n, k, dolls)

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(result)


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
    print_time_memory_data(main)
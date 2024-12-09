import os


def digit_sort(n, m, k, data):
    strings = ['' for _ in range(n)]
    for i in range(m):
        for j in range(n):
            strings[j] += data[i][j]

    indices = list(range(n))

    for phase in range(k):
        strings.sort(key=lambda x: x[m - phase - 1])
        indices = [i for _, i in sorted(zip(strings, indices))]

    return [i + 1 for i in indices]


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as infile:
        n, m, k = map(int, infile.readline().split())
        data = [infile.readline().strip() for _ in range(m)]

    result = digit_sort(n, m, k, data)

    with open(output_path, "w") as outfile:
        outfile.write(" ".join(map(str, result)))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

import os


def digit_sort(n, m, k, lines):

    indices = list(range(1, n + 1))

    for phase in range(1, k + 1):
        pos = m - phase
        indices.sort(key=lambda i: lines[pos][i - 1])

    return indices


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as infile:
        n, m, k = map(int, infile.readline().split())
        lines = [infile.readline().strip() for _ in range(m)]

    result = digit_sort(n, m, k, lines)

    with open(output_path, "w") as outfile:
        outfile.write(" ".join(map(str, result)))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

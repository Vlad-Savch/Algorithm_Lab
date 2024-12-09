import os


def generate_anti_quicksort(n):
    a = []
    for i in range(1, n + 1):
        mid = len(a) // 2
        a.insert(mid, i)
    return a


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, 'r') as infile:
        n = int(infile.readline().strip())

    anti_qs_array = generate_anti_quicksort(n)

    with open(output_path, 'w') as outfile:
        outfile.write(" ".join(map(str, anti_qs_array)))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
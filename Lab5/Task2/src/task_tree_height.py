import os
from utils import write_string_to_file, read_array_from_file


def calculate_tree_height(n, parents):
    from collections import defaultdict

    tree = defaultdict(list)
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def compute_height(node):
        if node not in tree:
            return 1
        return 1 + max(compute_height(child) for child in tree[node])

    return compute_height(root)


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as file:
        n = int(file.readline().strip())
        parents = list(map(int, file.readline().strip().split()))

    result = calculate_tree_height(n, parents)

    write_string_to_file(output_path, result)


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

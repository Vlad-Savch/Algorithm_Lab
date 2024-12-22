import math
import os


def is_fibonacci(n):
    n = int(n)

    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4

    return is_perfect_square(x1) or is_perfect_square(x2)


def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x


def process_queries(queries):
    results = []
    for query in queries:
        if is_fibonacci(query):
            results.append("Yes")
        else:
            results.append("No")
    return results


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, 'r') as f:
        n = int(f.readline().strip())
        queries = f.read().splitlines()

    results = process_queries(queries)

    with open(output_path, 'w') as f:
        f.write('\n'.join(results))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

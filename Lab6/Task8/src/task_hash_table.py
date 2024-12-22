import os


def process_hash_table(n, x, a, b, ac, bc, ad, bd):
    mod1 = 10 ** 3
    mod2 = 10 ** 15

    hash_table = set()

    for _ in range(n):
        if x in hash_table:
            a = (a + ac) % mod1
            b = (b + bc) % mod2
        else:
            hash_table.add(x)
            a = (a + ad) % mod1
            b = (b + bd) % mod2

        x = (x * a + b) % mod2

    return x, a, b


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, 'r') as f:
        n, x, a, b = map(int, f.readline().split())
        ac, bc, ad, bd = map(int, f.readline().split())

    result = process_hash_table(n, x, a, b, ac, bc, ad, bd)

    with open(output_path, 'w') as f:
        f.write(' '.join(map(str, result)))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

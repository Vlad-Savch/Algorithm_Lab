import os


def process_operations(operations):
    result = []
    s = set()

    for op in operations:
        if op[0] == 'A':
            _, x = op
            s.add(x)
        elif op[0] == 'D':
            _, x = op
            s.discard(x)
        elif op[0] == '?':
            _, x = op
            if x in s:
                result.append('Y')
            else:
                result.append('N')

    return result


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, 'r') as f:
        n = int(f.readline().strip())
        data = f.read().splitlines()

    operations = [line.split() for line in data]
    operations = [(op[0], int(op[1])) for op in operations]

    results = process_operations(operations)

    with open(output_path, 'w') as f:
        f.write('\n'.join(results))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

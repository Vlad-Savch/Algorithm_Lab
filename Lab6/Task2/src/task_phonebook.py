import os


def process_queries(queries):
    phonebook = {}
    results = []

    for query in queries:
        parts = query.split()
        command = parts[0]

        if command == "add":
            number = parts[1]
            name = parts[2]
            phonebook[number] = name

        elif command == "del":
            number = parts[1]
            if number in phonebook:
                del phonebook[number]

        elif command == "find":
            number = parts[1]
            if number in phonebook:
                results.append(phonebook[number])
            else:
                results.append("not found")

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

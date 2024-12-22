import os


def process_operations(operations):
    values = {}
    order = []
    result = []

    for operation in operations:
        parts = operation.split()
        command = parts[0]

        if command == "put":
            key, value = parts[1], parts[2]
            if key not in values:
                order.append(key)
            values[key] = value

        elif command == "get":
            key = parts[1]
            result.append(values.get(key, "<none>"))

        elif command == "prev":
            key = parts[1]
            if key not in values:
                result.append("<none>")
            else:
                index = order.index(key)
                if index == 0:
                    result.append("<none>")
                else:
                    result.append(values[order[index - 1]])

        elif command == "next":
            key = parts[1]
            if key not in values:
                result.append("<none>")
            else:
                index = order.index(key)
                if index == len(order) - 1:
                    result.append("<none>")
                else:
                    result.append(values[order[index + 1]])

        elif command == "delete":
            key = parts[1]
            if key in values:
                del values[key]
                order.remove(key)

    return result


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, 'r') as f:
        n = int(f.readline().strip())
        operations = f.read().splitlines()

    results = process_operations(operations)

    with open(output_path, 'w') as f:
        f.write('\n'.join(results))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()


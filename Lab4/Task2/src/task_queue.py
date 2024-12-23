from collections import deque
import os
from utils import print_time_memory_data


def queue_commands(commands):
    queue = deque()
    results = []

    for command in commands:
        if command.startswith('+'):
            _, number = command.split()
            queue.append(int(number))
        elif command == '-':
            if queue:
                results.append(queue.popleft())

    return results


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as infile:
        m = int(infile.readline().strip())
        commands = [infile.readline().strip() for _ in range(m)]

    results = queue_commands(commands)

    with open(output_path, "w") as outfile:
        for result in results:
            outfile.write(f"{result}\n")


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
    print_time_memory_data(main)

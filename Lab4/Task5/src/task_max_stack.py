import os
from utils import print_time_memory_data


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack:
            self.max_stack.append(value)
        else:
            self.max_stack.append(max(value, self.max_stack[-1]))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.max_stack.pop()

    def get_max(self):
        if self.max_stack:
            return self.max_stack[-1]


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    max_stack = MaxStack()
    with open(input_path, "r") as inf, open(output_path, "w") as outf:
        n = int(inf.readline().strip())
        for _ in range(n):
            command = inf.readline().strip().split()
            if command[0] == "push":
                max_stack.push(int(command[1]))
            elif command[0] == "pop":
                max_stack.pop()
            elif command[0] == "max":
                outf.write(f"{max_stack.get_max()}\n")


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
    print_time_memory_data(main)

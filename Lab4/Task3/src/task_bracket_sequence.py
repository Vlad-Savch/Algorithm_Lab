import os
from utils import print_time_memory_data


def bracket_sequence(sequence):
    stack = []
    matching_brackets = {')': '(', ']': '['}

    for char in sequence:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
    return not stack


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as inf, open(output_path, "w") as outf:
        n = int(inf.readline().strip())
        for _ in range(n):
            sequence = inf.readline().strip()
            if bracket_sequence(sequence):
                outf.write("YES\n")
            else:
                outf.write("NO\n")


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
    print_time_memory_data(main)
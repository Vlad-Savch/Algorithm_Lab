import os


def primitive_calculator(n):
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

    path = []
    current = n
    while current != 0:
        path.append(current)
        current = prev[current]
    path.reverse()

    return dp[n], path


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as fin:
        n = int(fin.readline().strip())

    operations, sequence = primitive_calculator(n)

    with open(output_path, "w") as fout:
        fout.write(f"{operations}\n")
        fout.write(" ".join(map(str, sequence)))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
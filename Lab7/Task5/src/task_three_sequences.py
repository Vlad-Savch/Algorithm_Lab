import os


def longest_common_subsequence_three(a, b, c):
    n = len(a)
    m = len(b)
    l = len(c)

    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as fin:
        n = int(fin.readline())
        a = list(map(int, fin.readline().split()))
        m = int(fin.readline())
        b = list(map(int, fin.readline().split()))
        l = int(fin.readline())
        c = list(map(int, fin.readline().split()))

    result = longest_common_subsequence_three(a, b, c)

    with open(output_path, "w") as fout:
        fout.write(str(result))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

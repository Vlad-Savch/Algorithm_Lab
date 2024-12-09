import os


def hirsch_index(citations):
    n = len(citations)
    citations.sort(reverse=True)
    h_index = 0

    for i in range(n):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as infile:
        line = infile.readline().strip()
        citations = [int(x) for x in line.replace(",", " ").split()]

    result = hirsch_index(citations)

    with open(output_path, "w") as outfile:
        outfile.write(str(result))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

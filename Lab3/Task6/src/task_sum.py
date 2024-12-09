import os
import heapq


def sum_of_tenth(n, m, A, B):
    products = []
    for a in A:
        for b in B:
            products.append(a * b)

    # Шаг 2: Сортировка произведений
    products.sort()

    # Шаг 3: Выбираем каждый 10-й элемент (начиная с первого, т.е. с индекса 0)
    sum_of_tenth_elements = 0
    for i in range(0, len(products), 10):  # Индексы с шагом 10, начиная с 0
        sum_of_tenth_elements += products[i]

    return sum_of_tenth_elements


def process_file(input_filename, output_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "../txtf", input_filename)
    output_path = os.path.join(base_dir, "../txtf", output_filename)

    with open(input_path, "r") as infile:
        n, m = map(int, infile.readline().split())
        A = list(map(int, infile.readline().split()))
        B = list(map(int, infile.readline().split()))

    result = sum_of_tenth(n, m, A, B)

    with open(output_path, "w") as outfile:
        outfile.write(str(result))


def main(input_filename="../txtf/input.txt", output_filename="../txtf/output.txt"):
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
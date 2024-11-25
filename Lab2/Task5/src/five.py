def majority_element(a, left, right):
    if left == right:
        return a[left]

    mid = (left + right) // 2
    left_candidate = majority_element(a, left, mid)
    right_candidate = majority_element(a, mid + 1, right)

    if left_candidate == right_candidate:
        return left_candidate

    left_count = sum(1 for i in range(left, right + 1) if a[i] == left_candidate)
    right_count = sum(1 for i in range(left, right + 1) if a[i] == right_candidate)

    if left_count > (right - left + 1) // 2:
        return left_candidate
    if right_count > (right - left + 1) // 2:
        return right_candidate

    return None


def solve(a):
    n = len(a)
    candidate = majority_element(a, 0, n - 1)

    if candidate is None:
        return 0

    count = sum(1 for x in a if x == candidate)
    if count > n // 2:
        return 1
    else:
        return 0


def main():
    with open("../../Task5/txtf/input.txt", "r") as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().strip().split()))

    result = solve(a)

    with open("../../Task5/txtf/output.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    main()

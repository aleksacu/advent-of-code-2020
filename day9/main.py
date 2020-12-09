import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        numbers = list(map(int, f.read().splitlines()))

    num = None
    for i in range(25, len(numbers)):
        pre = set()
        num = numbers[i]
        for j in range(i - 25, i):
            if num - numbers[j] in pre:
                break
            pre.add(numbers[j])
        else:
            break

    ml = []
    for i in range(len(numbers) - 2):
        t = num - numbers[i]
        j = i + 1
        while t > 0:
            t -= numbers[j]
            j += 1

        if t == 0 and j - i > len(ml):
            ml = numbers[i:j]

    print("Part one:", num)
    print("Part two:", min(ml) + max(ml))


if __name__ == "__main__":
    main()

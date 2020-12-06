import operator
import os
from functools import reduce


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        answers = f.read().split("\n\n")

    anyone, everyone = 0, 0
    for group in answers:
        anyone += len(set(group) - {"\n"})
        everyone += len(reduce(operator.and_, map(set, group.splitlines())))

    print("Part one:", anyone)
    print("Part two:", everyone)


if __name__ == "__main__":
    main()

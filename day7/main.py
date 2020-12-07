import operator
import os
import re
from collections import defaultdict
from functools import reduce


def can_contain(dag, val):
    cc = dag[val]
    if cc:
        return cc | reduce(operator.or_, (can_contain(dag, v) for v in cc))
    return cc


def contains_count(dag, val):
    c = dag[val]
    if c:
        return sum(c.values()) + sum(contains_count(dag, k) * v for k, v in c.items())
    return 0


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        bags = f.read().splitlines()

    pattern = re.compile("(?P<num>[1-9]+) (?P<color>[a-zA-Z ]+[a-zA-Z]) bags?[,.]")
    can_be_contained = defaultdict(set)
    contains = defaultdict(dict)
    for bag in bags:
        color, colors = bag.split(" bags contain ")
        for n, c in re.findall(pattern, colors):
            can_be_contained[c].add(color)
            contains[color][c] = int(n)

    print("Part one:", len(can_contain(can_be_contained, "shiny gold")))
    print("Part two:", contains_count(contains, "shiny gold"))


if __name__ == "__main__":
    main()

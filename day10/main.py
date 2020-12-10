import functools
import os


@functools.lru_cache(maxsize=None)
def num_combinations(ratings, i=0):
    if i >= len(ratings) - 1:
        return 1
    num = 0
    for j in range(1, 4):
        if i + j <= len(ratings) - 1 and ratings[i + j] - ratings[i] <= 3:
            num += num_combinations(ratings, i + j)
    return num


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        ratings = list(map(int, f.read().splitlines()))

    ratings.insert(0, 0)
    ratings.sort()

    one = 0
    three = 1

    for i in range(len(ratings) - 1):
        curr, nxt = ratings[i + 1], ratings[i]
        if curr - nxt == 1:
            one += 1
        elif curr - nxt == 3:
            three += 1

    print("Part one:", one * three)
    print("Part two:", num_combinations(tuple(ratings)))


if __name__ == "__main__":
    main()

def count_trees(map_, r, d):
    width = len(map_[0])
    height = len(map_)

    count = 0

    x = r
    for y in range(d, height, d):
        if (map_[y][x]) == "#":
            count += 1
        x += r
        x %= width

    return count


def main():
    with open("input.txt") as f:
        map_ = f.read().splitlines()

    print(f"Part one: {count_trees(map_, 3, 1)}")

    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    prod = 1
    for slope in slopes:
        prod *= count_trees(map_, *slope)

    print(f"Part two: {prod}")


if __name__ == "__main__":
    main()

import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        bps = f.read().splitlines()

    trr, trc = str.maketrans({"F": "0", "B": "1"}), str.maketrans({"L": "0", "R": "1"})
    ids = {
        8 * int(bp[:7].translate(trr), 2) + int(bp[7:].translate(trc), 2) for bp in bps
    }

    print("Part one:", max(ids))
    print(
        "Part two:",
        next(filter(lambda id_: id_ - 2 in ids and id_ - 1 not in ids, ids)) - 1,
    )


if __name__ == "__main__":
    main()

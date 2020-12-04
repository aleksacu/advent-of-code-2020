import re


def main():
    with open("input.txt") as f:
        passports = f.read().split("\n\n")

    required_fields = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    )

    required_field_validations = {
        "byr": re.compile("^(?:19[0-9][0-9])|(?:200[0-2])$"),
        "iyr": re.compile("^20(?:1[0-9]|20)$"),
        "eyr": re.compile("^20(?:2[0-9]|30)$"),
        "hgt": re.compile("^(?:1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)$"),
        "hcl": re.compile("^#[0-9a-f]{6}$"),
        "ecl": re.compile("^(?:amb|blu|brn|gry|grn|hzl|oth)$"),
        "pid": re.compile("^[0-9]{9}$"),
    }

    num_valid = 0
    num_really_valid = 0
    for passport in passports:
        if all(field in passport for field in required_fields):
            num_valid += 1
            for field in passport.split():
                name, value = field.split(":", 1)
                if name == "cid":
                    continue
                if not re.match(required_field_validations[name], value):
                    break
            else:
                num_really_valid += 1

    print(f"Part one: {num_valid}")
    print(f"Part one: {num_really_valid}")


if __name__ == "__main__":
    main()

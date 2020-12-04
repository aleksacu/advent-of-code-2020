use regex::Regex;
use std::collections::HashMap;

fn compile_re(pattern: &str) -> Regex {
    Regex::new(pattern).unwrap()
}

fn main() {
    let passports = include_str!("./input.txt")
        .split("\n\n")
        .collect::<Vec<&str>>();

    let required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

    let required_field_validations: HashMap<&str, Regex> = [
        ("byr", compile_re("^(?:19[0-9][0-9])|(?:200[0-2])$")),
        ("iyr", compile_re("^20(?:1[0-9]|20)$")),
        ("eyr", compile_re("^20(?:2[0-9]|30)$")),
        (
            "hgt",
            compile_re("^(?:1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)$"),
        ),
        ("hcl", compile_re("^#[0-9a-f]{6}$")),
        ("ecl", compile_re("^(?:amb|blu|brn|gry|grn|hzl|oth)$")),
        ("pid", compile_re("^[0-9]{9}$")),
    ]
    .iter()
    .cloned()
    .collect();

    let mut num_valid = 0;
    let mut invalid = 0;
    'outer: for passport in passports {
        for req_field in required_fields.iter() {
            if !passport.contains(req_field) {
                continue 'outer;
            }
        }
        num_valid += 1;
        for field in passport.split_whitespace() {
            let mut split_field = field.splitn(2, ':');
            let name = split_field.next().unwrap();
            let value = split_field.next().unwrap();
            if name == "cid" {
                continue;
            }
            if !required_field_validations[name].is_match(value) {
                invalid += 1;
                break;
            }
        }
    }

    println!("Part one: {}", num_valid);
    println!("Part one: {}", num_valid - invalid);
}

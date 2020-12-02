use regex::Regex;

fn count(passwords: &str) -> (i32, i32) {
    let mut part_one = 0;
    let mut part_two = 0;

    let pattern = Regex::new(
        "(?P<min>[1-9][0-9]*)\\-(?P<max>[1-9][0-9]*) (?P<letter>[a-z]): (?P<password>[a-z]+)\n",
    )
    .unwrap();

    for capture in pattern.captures_iter(passwords) {
        let min = capture.get(1).unwrap().as_str().parse::<i32>().unwrap();
        let max = capture.get(2).unwrap().as_str().parse::<i32>().unwrap();
        let letter = capture.get(3).unwrap().as_str().chars().next().unwrap();
        let password = capture.get(4).unwrap().as_str();

        let mut num_occurences = 0;
        for l in password.chars() {
            if l == letter {
                num_occurences += 1;
            }
        }
        if num_occurences >= min && num_occurences <= max {
            part_one += 1;
        }

        if (password.chars().nth(min as usize - 1).unwrap() == letter)
            != (password.chars().nth(max as usize - 1).unwrap() == letter)
        {
            part_two += 1;
        }
    }

    (part_one, part_two)
}

fn main() {
    let passwords = include_str!("./input.txt");
    let (part_one, part_two) = count(passwords);
    println!("Part one: {}", part_one);
    println!("Part two: {}", part_two);
}

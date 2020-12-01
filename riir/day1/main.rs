fn part_one(entries: &[i32]) -> i32 {
    for (i, v) in entries.iter().enumerate() {
        for e in &entries[i + 1..] {
            if v + e == 2020 {
                return v * e;
            }
        }
    }
    -1
}

fn part_two(entries: &[i32]) -> i32 {
    for (i, v) in entries.iter().enumerate() {
        for (j, e) in entries[i + 1..].iter().enumerate() {
            for n in &entries[j + 1..] {
                if v + e + n == 2020 {
                    return v * e * n;
                }
            }
        }
    }
    -1
}

fn main() {
    let entries: Vec<i32> = include_str!("./input.txt")
        .lines()
        .map(|entry| entry.parse::<i32>().unwrap())
        .collect();

    let mut solution = part_one(&entries);
    if solution == -1 {
        println!("No two entries sum up to 2020");
    } else {
        println!("Part one: {}", solution);
    }

    solution = part_two(&entries);
    if solution == -1 {
        println!("No three entries sum up to 2020");
    } else {
        println!("Part two: {}", solution);
    }
}

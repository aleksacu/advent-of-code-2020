use std::collections::HashSet;

fn get_id(bp: &str) -> i32 {
    let mut row = 0;
    let mut col = 0;
    for i in 0..=6 {
        row += (1 << (6 - i)) * (('F' as i32 - bp.chars().nth(i).unwrap() as i32) >> 2);
    }
    for i in 7..10 {
        col += (1 << (9 - i)) * (('R' as i32 - bp.chars().nth(i).unwrap() as i32) >> 2 ^ 1);
    }
    8 * row + col
}

fn main() {
    let bps = include_str!("./input.txt").lines().collect::<Vec<&str>>();

    let mut max = 0;
    let mut ids: HashSet<i32> = HashSet::new();

    for bp in bps {
        let id = get_id(bp);
        if id > max {
            max = id;
        }
        ids.insert(id);
    }

    let mut missing = -1;
    for id in ids.iter() {
        if ids.contains(&(id - 2)) && !ids.contains(&(id - 1)) {
            missing = id - 1;
        }
    }

    println!("Part one: {}", max);
    println!("Part two: {}", missing);
}

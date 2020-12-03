fn count_trees(map: &[&str], r: usize, d: usize) -> u32 {
    let width = map[0].len();
    let height = map.len();

    let mut count: u32 = 0;

    let mut x = r;
    for y in (d..height).step_by(d) {
        if map[y].chars().nth(x).unwrap() == '#' {
            count += 1;
        }
        x = (x + r) % width;
    }

    count
}

fn main() {
    let map = include_str!("./input.txt").lines().collect::<Vec<&str>>();

    println!("Part one: {}", count_trees(&map, 3, 1));

    let slopes: [(usize, usize); 5] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];

    let mut prod: u32 = 1;
    for &(r, d) in slopes.iter() {
        prod *= count_trees(&map, r, d);
    }
    println!("Part two: {}", prod);
}

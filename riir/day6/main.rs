fn main() {
    let answers = include_str!("./input.txt")
        .split("\n\n")
        .collect::<Vec<&str>>();

    let mut anyone = 0;
    let mut everyone = 0;

    for group in answers {
        let mut counter = [0; 26];
        let mut num_people = 0;
        for person in group.split('\n') {
            for char in person.chars() {
                counter[char as usize - 'a' as usize] += 1;
            }
            num_people += 1;
        }
        for &count in counter.iter() {
            if count != 0 {
                anyone += 1;
                if count == num_people {
                    everyone += 1;
                }
            }
        }
    }

    println!("Part one: {}", anyone);
    println!("Part one: {}", everyone);
}

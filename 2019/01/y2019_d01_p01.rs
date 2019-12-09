use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let handle = stdin.lock();

    let ans: i64 = handle
        .lines()
        .map(|l| l.unwrap().parse::<i64>().unwrap())
        .map(|x| (x / 3) - 2)
        .sum();

    println!("{}", ans);
}

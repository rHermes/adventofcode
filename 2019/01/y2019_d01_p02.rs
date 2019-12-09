use std::io::{self, BufRead};

// n is current, a is acummulated
fn solve(n: i64, a: i64) -> i64 {
    let i = (n / 3) - 2;
    if i > 0 {
        solve(i, a + i)
    } else {
        a
    }
}

fn main() {
    let stdin = io::stdin();
    let handle = stdin.lock();

    let ans: i64 = handle
        .lines()
        .map(|l| l.unwrap().parse().unwrap())
        .map(|l| solve(l, 0))
        .sum();

    println!("{}", ans);
}

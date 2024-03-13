// Created by Jones at 2024/03/13 13:04
// leetgo: 1.4.2
// https://leetcode.com/problems/find-the-pivot-integer/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        // sum(1..=x) = sum(x..=n)
        // (1 +  x) * x  == (x + n) * (n-x+1)
        //  x^2 == -x^2 +  n*n + n
        //  2 * x * x == n * n + n
        let x = (((n * n + n) / 2) as f64).sqrt() as i32;
        if 2 * x * x == n * n + n {
            return x;
        }
        -1
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::pivot_integer(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

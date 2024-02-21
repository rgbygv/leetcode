// Created by Jones at 2024/02/21 12:48
// leetgo: 1.4.1
// https://leetcode.com/problems/bitwise-and-of-numbers-range/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        if left == 0 {
            return 0;
        }
        let n1 = 31 - left.leading_zeros();
        let n2 = 31 - right.leading_zeros();
        // println!("{left} {right} {n1} {n2}");
        if n1 != n2 {
            return 0;
        }
        (1 << n1) | Solution::range_bitwise_and(left ^ (1 << n1), right ^ (1 << n2))
    }
}

// @lc code=end

fn main() -> Result<()> {
    let left: i32 = deserialize(&read_line()?)?;
    let right: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::range_bitwise_and(left, right).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/03/31 20:28
// leetgo: 1.4.3
// https://leetcode.cn/problems/harshad-number/
// https://leetcode.cn/contest/weekly-contest-391/problems/harshad-number/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn sum_of_the_digits_of_harshad_number(x: i32) -> i32 {
        let sum = x
            .to_string()
            .chars()
            .map(|ch| (ch as u8 - b'0') as i32)
            .sum();
        if x % sum == 0 {
            return sum;
        }
        -1
    }
}

// @lc code=end

fn main() -> Result<()> {
    let x: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::sum_of_the_digits_of_harshad_number(x).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

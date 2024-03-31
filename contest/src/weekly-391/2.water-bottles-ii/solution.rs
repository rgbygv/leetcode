// Created by Jones at 2024/03/31 20:28
// leetgo: 1.4.3
// https://leetcode.cn/problems/water-bottles-ii/
// https://leetcode.cn/contest/weekly-contest-391/problems/water-bottles-ii/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_bottles_drunk(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut x = num_bottles;
        let mut y = num_exchange;

        let mut res = x;
        while x >= y {
            res += 1;
            x -= y - 1;
            y += 1;
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let num_bottles: i32 = deserialize(&read_line()?)?;
    let num_exchange: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_bottles_drunk(num_bottles, num_exchange).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

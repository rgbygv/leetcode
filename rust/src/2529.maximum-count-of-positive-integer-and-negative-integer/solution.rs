// Created by Jones at 2024/04/09 13:52
// leetgo: 1.4.5
// https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_count(nums: Vec<i32>) -> i32 {
        let i = nums.partition_point(|y| *y < 0);
        let j = nums.partition_point(|y| *y <= 0);

        let n = nums.len();

        (n - j).max(i) as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_count(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

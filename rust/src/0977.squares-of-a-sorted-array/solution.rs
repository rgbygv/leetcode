// Created by Jones at 2024/03/02 13:47
// leetgo: 1.4.1
// https://leetcode.com/problems/squares-of-a-sorted-array/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut a = nums;
        a.sort_unstable_by_key(|x| x.abs());
        a.into_iter().map(|x| x * x).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::sorted_squares(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

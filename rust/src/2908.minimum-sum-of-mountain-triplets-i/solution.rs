// Created by Jones at 2024/03/29 13:54
// leetgo: 1.4.3
// https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {

    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let ans: i32 = Solution::minimum_sum(nums).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

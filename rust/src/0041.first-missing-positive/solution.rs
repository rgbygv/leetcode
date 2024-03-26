// Created by Jones at 2024/03/26 11:52
// leetgo: 1.4.3
// https://leetcode.com/problems/first-missing-positive/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let ans: i32 = Solution::first_missing_positive(nums).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

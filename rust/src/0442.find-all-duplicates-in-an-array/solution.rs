// Created by Jones at 2024/03/25 15:22
// leetgo: 1.4.3
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_duplicates(nums: Vec<i32>) -> Vec<i32> {
        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let ans: Vec<i32> = Solution::find_duplicates(nums).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

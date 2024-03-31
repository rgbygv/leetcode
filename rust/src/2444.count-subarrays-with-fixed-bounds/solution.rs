// Created by Jones at 2024/03/31 14:08
// leetgo: 1.4.3
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let min_k: i32 = deserialize(&read_line()?)?;
	let max_k: i32 = deserialize(&read_line()?)?;
	let ans: i64 = Solution::count_subarrays(nums, min_k, max_k).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

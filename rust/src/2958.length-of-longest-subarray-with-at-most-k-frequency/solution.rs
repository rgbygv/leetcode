// Created by Jones at 2024/03/28 15:12
// leetgo: 1.4.3
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let k: i32 = deserialize(&read_line()?)?;
	let ans: i32 = Solution::max_subarray_length(nums, k).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

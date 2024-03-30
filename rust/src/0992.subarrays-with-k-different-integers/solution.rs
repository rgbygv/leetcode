// Created by Jones at 2024/03/30 11:01
// leetgo: 1.4.3
// https://leetcode.com/problems/subarrays-with-k-different-integers/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let k: i32 = deserialize(&read_line()?)?;
	let ans: i32 = Solution::subarrays_with_kdistinct(nums, k).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

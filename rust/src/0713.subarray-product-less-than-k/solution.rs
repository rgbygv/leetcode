// Created by Jones at 2024/03/27 14:21
// leetgo: 1.4.3
// https://leetcode.com/problems/subarray-product-less-than-k/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let k: i32 = deserialize(&read_line()?)?;
	let ans: i32 = Solution::num_subarray_product_less_than_k(nums, k).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

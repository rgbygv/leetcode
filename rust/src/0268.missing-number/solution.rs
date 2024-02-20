// Created by Jones at 2024/02/20 17:50
// leetgo: 1.4.1
// https://leetcode.com/problems/missing-number/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
		let n = nums.len() as i32;
		let s = nums.iter().sum::<i32>();
		
		(n+1) * n / 2 - s
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums: Vec<i32> = deserialize(&read_line()?)?;
	let ans: i32 = Solution::missing_number(nums).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

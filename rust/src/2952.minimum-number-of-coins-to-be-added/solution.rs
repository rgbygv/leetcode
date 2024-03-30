// Created by Jones at 2024/03/30 10:41
// leetgo: 1.4.3
// https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_added_coins(coins: Vec<i32>, target: i32) -> i32 {

    }
}

// @lc code=end

fn main() -> Result<()> {
	let coins: Vec<i32> = deserialize(&read_line()?)?;
	let target: i32 = deserialize(&read_line()?)?;
	let ans: i32 = Solution::minimum_added_coins(coins, target).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

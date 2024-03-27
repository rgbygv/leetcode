// Created by Jones at 2024/03/27 14:08
// leetgo: 1.4.3
// https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_ways(ranges: Vec<Vec<i32>>) -> i32 {

    }
}

// @lc code=end

fn main() -> Result<()> {
	let ranges: Vec<Vec<i32>> = deserialize(&read_line()?)?;
	let ans: i32 = Solution::count_ways(ranges).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

// Created by Jones at 2024/03/31 13:50
// leetgo: 1.4.3
// https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn is_valid_serialization(preorder: String) -> bool {

    }
}

// @lc code=end

fn main() -> Result<()> {
	let preorder: String = deserialize(&read_line()?)?;
	let ans: bool = Solution::is_valid_serialization(preorder).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

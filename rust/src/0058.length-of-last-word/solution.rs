// Created by Jones at 2024/04/01 11:50
// leetgo: 1.4.3
// https://leetcode.com/problems/length-of-last-word/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        s.split_ascii_whitespace().last().unwrap().len() as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::length_of_last_word(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

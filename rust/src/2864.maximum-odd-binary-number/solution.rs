// Created by Jones at 2024/03/01 11:16
// leetgo: 1.4.1
// https://leetcode.com/problems/maximum-odd-binary-number/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let n = s.len();
        let cnt = s.bytes().filter(|ch| *ch == b'1').count();
        format!("{}{}1", "1".repeat(cnt - 1), "0".repeat(n - cnt))
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: String = Solution::maximum_odd_binary_number(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

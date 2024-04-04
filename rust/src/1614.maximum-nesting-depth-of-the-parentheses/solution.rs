// Created by Jones at 2024/04/04 15:13
// leetgo: 1.4.3
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut bal = 0;
        let mut res = 0;

        for ch in s.chars() {
            if ch == '(' {
                bal += 1;
                res = res.max(bal);
            } else if ch == ')' {
                bal -= 1;
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_depth(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

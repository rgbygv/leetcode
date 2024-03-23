// Created by Jones at 2024/03/23 13:42
// leetgo: 1.4.3
// https://leetcode.cn/problems/count-distinct-numbers-on-board/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn distinct_integers(n: i32) -> i32 {
        if n == 1 {
            1
        } else {
            n - 1
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::distinct_integers(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/04/10 13:43
// leetgo: 1.4.5
// https://leetcode.cn/problems/maximum-binary-string-after-change/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_binary_string(binary: String) -> String {
        //  00 -> 10, 10 -> 01
        let mut pos = vec![];
        for (i, ch) in binary.char_indices() {
            if ch == '0' {
                pos.push(i)
            }
        }
        let n = pos.len();
        // can't use op1, don't need use op2
        if n < 2 {
            return binary;
        }
        let first = pos[0];

        format!(
            "{}{}0{}",
            "1".repeat(first),
            "1".repeat(n - 1),
            "1".repeat(binary.len() - first - n)
        )
    }
}

// @lc code=end

fn main() -> Result<()> {
    let binary: String = deserialize(&read_line()?)?;
    let ans: String = Solution::maximum_binary_string(binary).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

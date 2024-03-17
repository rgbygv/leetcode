// Created by Jones at 2024/03/17 21:45
// leetgo: 1.4.2
// https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse/
// https://leetcode.cn/contest/weekly-contest-389/problems/existence-of-a-substring-in-a-string-and-its-reverse/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn is_substring_present(s: String) -> bool {
        let rs: String = s.chars().rev().collect();
        for i in 2..=s.len() {
            let cur = s.get(i - 2..i).unwrap();
            if rs.contains(cur) {
                return true;
            }
        }
        false
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_substring_present(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

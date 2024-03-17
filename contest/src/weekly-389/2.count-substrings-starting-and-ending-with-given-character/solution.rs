// Created by Jones at 2024/03/17 21:45
// leetgo: 1.4.2
// https://leetcode.cn/problems/count-substrings-starting-and-ending-with-given-character/
// https://leetcode.cn/contest/weekly-contest-389/problems/count-substrings-starting-and-ending-with-given-character/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_substrings(s: String, c: char) -> i64 {
        let cnt = s.chars().filter(|ch| *ch == c).count();
        ((cnt + 1) * cnt / 2) as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let c: char = deserialize(&read_line()?)?;
    let ans: i64 = Solution::count_substrings(s, c).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

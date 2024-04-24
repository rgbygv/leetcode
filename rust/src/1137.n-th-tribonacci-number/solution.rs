// Created by Jones at 2024/04/24 09:31
// leetgo: 1.4.5
// https://leetcode.com/problems/n-th-tribonacci-number/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        if n < 3 {
            let v = [0, 1, 1];
            return v[n as usize];
        }

        let (mut a, mut b, mut c) = (0, 1, 1);
        for _ in 3..=n {
            (a, b, c) = (b, c, a + b + c)
        }
        c
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::tribonacci(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

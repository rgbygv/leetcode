// Created by Jones at 2024/04/02 13:25
// leetgo: 1.4.3
// https://leetcode.com/problems/isomorphic-strings/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut s2t = HashMap::new();
        let mut t2s = HashMap::new();

        for (x, y) in s.bytes().zip(t.bytes()) {
            if let Some(v) = s2t.get_mut(&x) {
                if *v != y {
                    return false;
                }
            } else {
                s2t.insert(x, y);
            }
            if let Some(v) = t2s.get_mut(&y) {
                if *v != x {
                    return false;
                }
            } else {
                t2s.insert(y, x);
            }
        }
        true
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let t: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_isomorphic(s, t).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

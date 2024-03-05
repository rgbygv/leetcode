// Created by Jones at 2024/03/05 19:12
// leetgo: 1.4.1
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let n = s.len();
        let s = s.into_bytes();

        let mut l = 0;
        let mut r = n - 1;
        while l <= r {
            if s[l] != s[r] || l == r {
                return (r - l + 1) as _;
            }
            let x = s[l];
            while l < r && s[l] == x {
                l += 1;
            }
			if l == r{
				return 0;
			}
            while l < r && s[r] == x {
                r -= 1;
            }
        }
        unreachable!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_length(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

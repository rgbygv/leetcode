// Created by Jones at 2024/04/07 12:04
// leetgo: 1.4.5
// https://leetcode.com/problems/valid-parenthesis-string/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut st = vec![];

        let mut p = vec![];
        for (i, ch) in s.char_indices() {
            match ch {
                '*' => st.push(i),
                '(' => p.push(i),
                _ => {
                    if p.len() > 0 {
                        p.pop();
                    } else if st.len() > 0 {
                        st.pop();
                    } else {
                        return false;
                    }
                }
            }
        }

        if p.len() > st.len() {
            return false;
        }
        while let (Some(x), Some(y)) = (p.pop(), st.pop()) {
            if x > y {
                return false;
            }
        }

        true
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::check_valid_string(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

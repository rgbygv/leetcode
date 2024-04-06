// Created by Jones at 2024/04/06 08:47
// leetgo: 1.4.5
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let mut st = vec![];
        let mut f = vec![false; s.len()]; // whether delete

        for (i, ch) in s.char_indices() {
            if ch == '(' {
                st.push(i)
            } else if ch == ')' {
                if st.is_empty() {
                    f[i] = true
                } else {
                    st.pop();
                }
            }
        }
        // these '(' can't find ')'
        for i in st {
            f[i] = true;
        }

        // s.char_indices()
        //     .map(|(i, ch)| if !f[i] { ch.to_string() } else { String::new() })
        //     .collect()

        let mut res = String::new();
        s.char_indices().for_each(|(i, ch)| {
            if !f[i] {
                res.push(ch)
            }
        });

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: String = Solution::min_remove_to_make_valid(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

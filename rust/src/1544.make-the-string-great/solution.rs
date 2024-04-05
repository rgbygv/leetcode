// Created by Jones at 2024/04/05 15:56
// leetgo: 1.4.5
// https://leetcode.com/problems/make-the-string-great/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn make_good(s: String) -> String {
        let mut st = vec![];
        for ch in s.bytes() {
            let mut ok = true;
            if let Some(last) = st.last() {
                if ch + 32 == *last || *last + 32 == ch {
                    ok = false;
                    st.pop();
                }
            }
            if ok {
                st.push(ch)
            }
        }

        unsafe { String::from_utf8_unchecked(st) }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: String = Solution::make_good(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

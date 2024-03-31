// Created by Jones at 2024/03/31 13:50
// leetgo: 1.4.3
// https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn is_valid_serialization(preorder: String) -> bool {
        let s: Vec<_> = preorder.split(',').collect();

        let null = "#";

        if s[0] == null {
            return s.len() == 1;
        }

        let mut st = vec![];
        st.push((s[0], 0));

        for i in 1..s.len() {
            while !st.is_empty() && st.last().unwrap().1 == 2 {
                st.pop();
            }
            if let Some((root, cnt)) = st.pop() {
                if s[i] == null {
                    if cnt <= 1 {
                        st.push((root, cnt + 1))
                    }
                } else {
                    st.push((root, cnt + 1));
                    st.push((s[i], 0))
                }
            } else {
                return false;
            }
        }
        while !st.is_empty() && st.last().unwrap().1 == 2 {
            st.pop();
        }
        // println!("{:?}", st);
        st.is_empty()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let preorder: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_valid_serialization(preorder).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

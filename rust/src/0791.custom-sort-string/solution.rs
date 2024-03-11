// Created by Jones at 2024/03/11 13:15
// leetgo: 1.4.1
// https://leetcode.cn/problems/custom-sort-string/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut map = vec![26; 26];

        order.char_indices().for_each(|(i, ch)| {
            map[ch as usize - 'a' as usize] = i;
        });

        let mut s: Vec<_> = s.chars().collect();
        s.sort_unstable_by_key(|ch| map[*ch as usize - 'a' as usize]);

        s.into_iter().collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let order: String = deserialize(&read_line()?)?;
    let s: String = deserialize(&read_line()?)?;
    let ans: String = Solution::custom_sort_string(order, s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

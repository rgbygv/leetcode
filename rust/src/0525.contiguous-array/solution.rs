// Created by Jones at 2024/03/16 13:22
// leetgo: 1.4.2
// https://leetcode.com/problems/contiguous-array/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        let mut pos = HashMap::new();
        pos.insert(0, -1);
        let mut s = 0;
        let mut res = 0;
        for (i, x) in nums.into_iter().enumerate() {
            let i = i as i32;
            if x == 0 {
                s -= 1;
            } else {
                s += 1;
            }
            res = res.max(i - pos.get(&s).unwrap_or(&i));
            if !pos.contains_key(&s) {
                pos.insert(s, i);
            }
        }
        res
    }
}
// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_max_length(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

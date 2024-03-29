// Created by Jones at 2024/03/29 14:07
// leetgo: 1.4.3
// https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let max = *nums.iter().max().unwrap();
        let k = k as usize;
        let mut pos = vec![];
        let mut res = 0;
        let mut last = 0;
        for (i, x) in nums.into_iter().enumerate() {
            if x == max {
                pos.push(i);
                // println!("{pos:?}");
                let n = pos.len();
                if n >= k {
                    last = pos[n - k] + 1;
                    res += last;
                }
            } else {
                res += last;
            }
        }

        res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i64 = Solution::count_subarrays(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

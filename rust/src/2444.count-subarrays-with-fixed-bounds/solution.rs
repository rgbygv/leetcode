// Created by Jones at 2024/03/31 14:08
// leetgo: 1.4.3
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let handle = |i: usize, j: usize| -> i64 {
            let mut last_min = None;
            let mut last_max = None;
            let mut res = 0;

            for k in i..=j {
                if nums[k] == min_k {
                    last_min = Some(k);
                }
                if nums[k] == max_k {
                    last_max = Some(k);
                }

                if let (Some(x), Some(y)) = (last_min, last_max) {
                    res += x.min(y) - i + 1;
                }
            }
            res as _
        };

        let n = nums.len();

        let mut res = 0;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && nums[j] >= min_k && nums[j] <= max_k {
                j += 1;
            }
            if i == j {
                i += 1
            } else {
                // println!("{} {}", i , j);
                res += handle(i, j - 1);
                i = j
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let min_k: i32 = deserialize(&read_line()?)?;
    let max_k: i32 = deserialize(&read_line()?)?;
    let ans: i64 = Solution::count_subarrays(nums, min_k, max_k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

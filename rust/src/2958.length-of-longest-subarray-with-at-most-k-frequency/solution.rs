// Created by Jones at 2024/03/28 15:12
// leetgo: 1.4.3
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut l = 0;
        let mut cnt = HashMap::new();
        let mut res = 0;

        for (r, &x) in nums.iter().enumerate() {
            *cnt.entry(x).or_insert(0) += 1;
            while cnt[&x] > k {
                *cnt.get_mut(&nums[l]).unwrap() -= 1;
                l += 1;
            }
            res = res.max(r - l + 1);
        }
        res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_subarray_length(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

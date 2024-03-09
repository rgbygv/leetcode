// Created by Jones at 2024/03/09 22:53
// leetgo: 1.4.1
// https://leetcode.cn/problems/minimum-common-value/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (m, n) = (nums1.len(), nums2.len());
        let (mut i, mut j) = (0, 0);
        while i < m && j < n {
            if nums1[i] == nums2[j] {
                return nums1[i];
            }
            if nums1[i] < nums2[j] {
                i += 1;
            } else {
                j += 1
            }
        }
        -1
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums1: Vec<i32> = deserialize(&read_line()?)?;
    let nums2: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::get_common(nums1, nums2).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

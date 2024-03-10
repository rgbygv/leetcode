// Created by Jones at 2024/03/10 12:11
// leetgo: 1.4.1
// https://leetcode.cn/problems/intersection-of-two-arrays/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut cnt = vec![0; 1001];
        for x in nums1 {
            cnt[x as usize] = 1;
        }

        let mut res = vec![];
        for x in nums2 {
            let x = x as usize;
            if cnt[x] > 0 {
                cnt[x] -= 1;
                res.push(x as i32)
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums1: Vec<i32> = deserialize(&read_line()?)?;
    let nums2: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::intersection(nums1, nums2).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

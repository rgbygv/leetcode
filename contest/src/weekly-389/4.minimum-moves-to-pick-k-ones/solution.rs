// Created by Jones at 2024/03/17 21:45
// leetgo: 1.4.2
// https://leetcode.cn/problems/minimum-moves-to-pick-k-ones/
// https://leetcode.cn/contest/weekly-contest-389/problems/minimum-moves-to-pick-k-ones/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn calc(size: usize) -> usize {
        if size & 1 == 1 {
            return (1 + size / 2) * size / 2;
        } else {
            return size / 2 + Self::calc(size - 1);
        }
    }
    pub fn minimum_moves(nums: Vec<i32>, k: i32, max_changes: i32) -> i64 {
        let (k, c) = (k as usize, max_changes as usize);
        if c >= k {
            return Self::calc(k as usize) as _;
        }
        let mut pos = vec![];
        for (i, &x) in nums.iter().enumerate() {
            if x == 1 {
                pos.push(i)
            }
        }
        // pos[l..r] + c == k
        let mut res = usize::MAX;
        for l in 0..pos.len() {
            let r = l + (k - c);
            if r >= pos.len() {
                break;
            }
            let size = pos[r] - pos[l];
            if size <= k {
                return Self::calc(size) as _;
            }
            res = res.min(Self::calc(size))
        }
        res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let max_changes: i32 = deserialize(&read_line()?)?;
    let ans: i64 = Solution::minimum_moves(nums, k, max_changes).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/03/14 13:11
// leetgo: 1.4.2
// https://leetcode.com/problems/binary-subarrays-with-sum/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        let mut cnt = HashMap::new();
        cnt.insert(0, 1);

        let mut s = 0;
        let mut res = 0;
        for x in nums {
            s += x;
            res += cnt.get(&(s - goal)).unwrap_or(&0);
            *cnt.entry(s).or_insert(0) += 1;
            // println!("{x} {res} {cnt:?}");
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let goal: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::num_subarrays_with_sum(nums, goal).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

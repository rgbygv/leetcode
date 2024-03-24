// Created by Jones at 2024/03/24 16:59
// leetgo: 1.4.3
// https://leetcode.com/problems/find-the-duplicate-number/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut fast = nums[nums[0] as usize];
        let mut slow = nums[0];
        while fast != slow {
            fast = nums[nums[fast as usize] as usize];
            slow = nums[slow as usize];
        }

        let mut head = 0;
        while head != slow {
            head = nums[head as usize];
            slow = nums[slow as usize];
        }

        head
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_duplicate(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

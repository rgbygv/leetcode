// Created by Jones at 2024/03/15 12:51
// leetgo: 1.4.2
// https://leetcode.com/problems/product-of-array-except-self/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = vec![1; n];
        (1..n).for_each(|i| res[i] = res[i - 1] * (nums[i - 1]));

        let mut right = nums[n - 1];
        for i in (0..n - 1).rev() {
            res[i] *= right;
            right *= nums[i];
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::product_except_self(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/03/27 14:21
// leetgo: 1.4.3
// https://leetcode.com/problems/subarray-product-less-than-k/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        // - `1 <= nums.length <= 3 * 10⁴`
        // - `1 <= nums[i] <= 1000`
        // - `0 <= k <= 10⁶`
        //
        if k <= 1 {
            return 0;
        }
        let mut l = 0;
        let mut x = 1;
        let mut res = 0;
        for (r, &y) in nums.iter().enumerate() {
            x *= y;
            while x >= k {
                x /= nums[l];
                l += 1;
            }
            res += r - l + 1;
        }
        res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::num_subarray_product_less_than_k(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

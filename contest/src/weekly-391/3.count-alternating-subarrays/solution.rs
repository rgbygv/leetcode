// Created by Jones at 2024/03/31 20:28
// leetgo: 1.4.3
// https://leetcode.cn/problems/count-alternating-subarrays/
// https://leetcode.cn/contest/weekly-contest-391/problems/count-alternating-subarrays/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_alternating_subarrays(nums: Vec<i32>) -> i64 {
        let mut res = 0;

        let n = nums.len();
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && nums[j] != nums[j - 1] {
                j += 1;
            }
            fn calc(len: usize) -> usize {
                len * (len + 1) / 2
            }
            res += calc(j - i) as i64;
            i = j;
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::count_alternating_subarrays(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

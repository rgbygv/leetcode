// Created by Jones at 2024/04/08 12:52
// leetgo: 1.4.5
// https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        // we can enumerate the start, and use SortedList to maintain the num in [start, start + n - 1]
        // start must in nums?

        let n = nums.len() as i32;
        let mut a: Vec<i32> = nums
            .into_iter()
            .collect::<HashSet<i32>>()
            .into_iter()
            .collect();
        a.sort_unstable();

        let mut res = n - 1;
        for (i, &x) in a.iter().enumerate() {
            let j = a.partition_point(|&y| y <= (x + n - 1));
            res = res.min(n - (j - i) as i32)
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_operations(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

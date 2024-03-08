// Created by Jones at 2024/03/08 20:18
// leetgo: 1.4.1
// https://leetcode.cn/problems/count-elements-with-maximum-frequency/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut cnt = vec![0; 101];
        for x in nums {
            cnt[x as usize] += 1;
        }
        let max_freq = cnt.iter().max().unwrap();
        cnt.iter().filter(|&x| x == max_freq).count() as i32 * max_freq
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_frequency_elements(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

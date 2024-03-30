// Created by Jones at 2024/03/30 10:41
// leetgo: 1.4.3
// https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_added_coins(coins: Vec<i32>, target: i32) -> i32 {
        let mut coins = coins;
        coins.sort_unstable();

        let mut res = 0;
        let mut s = 0;
        for x in coins {
            while s < target && s + 1 < x {
                res += 1;
                s = s * 2 + 1;
            }
            if s < target {
                s += x;
            }
        }

        while s < target {
            res += 1;
            s = s * 2 + 1;
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let coins: Vec<i32> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_added_coins(coins, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/03/25 11:21
// leetgo: 1.4.3
// https://leetcode.cn/problems/coin-change-ii/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let m = amount as usize;

        let mut f = vec![0; m + 1];
        f[0] = 1;

        // f[i][x] = f[i-1][x] + f[i-1][x -coins[i]]

        // O(m * len(coins))
        for c in coins {
            let c = c as usize;
            for x in c..=m {
                f[x] += f[x - c]
            }
        }

        f[m]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let amount: i32 = deserialize(&read_line()?)?;
    let coins: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::change(amount, coins).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

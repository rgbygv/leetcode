// Created by Jones at 2024/03/24 16:53
// leetgo: 1.4.3
// https://leetcode.cn/problems/coin-change/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let m = amount as usize;
        let inf = 1e9 as i32;
        let mut f = vec![inf; m + 1];
        f[0] = 0;

        for i in 1..=m {
            for &x in &coins {
                if i as i32 >= x {
                    f[i] = f[i].min(f[i - x as usize] + 1)
                }
            }
        }

        if f[m] >= inf {
            -1
        } else {
            f[m]
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let coins: Vec<i32> = deserialize(&read_line()?)?;
    let amount: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::coin_change(coins, amount).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

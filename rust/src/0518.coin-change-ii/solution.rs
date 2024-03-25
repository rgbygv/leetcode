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

        // O(m*m)
        for c in coins {
            let c = c as usize;
            for x in (1..=m).rev() {
                for y in (c..=m / c * c).rev().step_by(c) {
                    // println!("{x} {y} {c}");
                    if x >= y {
                        f[x] += f[x - y]
                    }
                }
            }
        }
        // println!("{f:?}");
        f[m]

        // for x in 1..=m {
        //     for &y in &coins {
        //         let y = y as usize;
        //         if x >= y {
        //             f[x] += f[x - y];
        //         }
        //     }
        // }
        // println!("{f:?}");

        // f[m]
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

// Created by Jones at 2024/04/10 14:21
// leetgo: 1.4.5
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn deck_revealed_increasing(mut deck: Vec<i32>) -> Vec<i32> {
        deck.sort_unstable();
        let n = deck.len();
        let mut res = vec![0; n];

        let mut i = 0;
        for j in 0..n {
            if res[i] == 0 {
                res[i] = deck[j];
                if j == n - 1 {
                    break;
                }
                let mut step = 2;
                while step > 0 {
                    println!("{i}");
                    i = (i + 1) % n;
                    if res[i] == 0 {
                        step -= 1
                    }
                }
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let deck: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::deck_revealed_increasing(deck).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

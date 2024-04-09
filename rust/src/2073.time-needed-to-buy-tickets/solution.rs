// Created by Jones at 2024/04/09 17:16
// leetgo: 1.4.5
// https://leetcode.com/problems/time-needed-to-buy-tickets/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let mut deque = VecDeque::new();
        let k = k as usize;
        if tickets[k] == 0 {
            return 0;
        }

        for (i, x) in tickets.into_iter().enumerate() {
            deque.push_back((i, x))
        }

        let mut t = 0;
        while let Some((i, x)) = deque.pop_front() {
            t += 1;
            let y = x - 1;
            if y == 0 {
                if i == k {
                    return t;
                }
            } else {
                deque.push_back((i, y))
            }
        }

        t
    }
}

// @lc code=end

fn main() -> Result<()> {
    let tickets: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::time_required_to_buy(tickets, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/03/28 14:40
// leetgo: 1.4.3
// https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn first_day_been_in_all_rooms(next_visit: Vec<i32>) -> i32 {
        let m = 1e9 as usize + 7;

        let n = next_visit.len();
        let mut f = vec![0; n];

        for i in 1..n {
            let j = next_visit[i - 1] as usize;
            f[i] = f[i - 1] + 2;
            if j != i - 1 {
                f[i] += (f[i - 1] + m - f[j]) % m
            }
            f[i] %= m;
        }
        // println!("{f:?}");
        (f[n - 1]) as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let next_visit: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::first_day_been_in_all_rooms(next_visit).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

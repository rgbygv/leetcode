// Created by Jones at 2024/03/18 14:06
// leetgo: 1.4.2
// https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
        points.sort_unstable_by_key(|e| e[1]);
        let mut res = 1;
        let mut r = points[0][1];
        points.iter().for_each(|point| {
            if point[0] > r {
                res += 1;
                r = point[1];
            }
        });
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let points: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_min_arrow_shots(points).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

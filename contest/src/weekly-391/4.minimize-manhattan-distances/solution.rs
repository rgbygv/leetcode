// Created by Jones at 2024/03/31 20:28
// leetgo: 1.4.3
// https://leetcode.cn/problems/minimize-manhattan-distances/
// https://leetcode.cn/contest/weekly-contest-391/problems/minimize-manhattan-distances/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_distance(mut points: Vec<Vec<i32>>) -> i32 {
        points.sort_unstable();
        // the removed point must have max_x or max_y or min_x or min_y
        let calc = |i: usize, j: usize| -> i32 {
            let (x, y) = (&points[i], &points[j]);

            (x[0] - y[0]).abs() + (x[1] - y[1]).abs()
        };

		
        // let (mut l, mut r) = (0, 2e8 as i32 + 1);

        // while l < r {
        // 	let mid = (l+r) >> 1;
        // 	let check = |mid:i32| -> bool{

        // 		todo!()
        // 	};

        // }

        // todo!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let points: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_distance(points).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

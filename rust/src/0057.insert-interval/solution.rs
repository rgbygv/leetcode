// Created by Jones at 2024/03/17 13:16
// leetgo: 1.4.2
// https://leetcode.cn/problems/insert-interval/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let n = intervals.len();
        if n == 0 {
            return vec![new_interval];
        }
        let (mut l, mut r) = (new_interval[0], new_interval[1]);
        let mut res = vec![];
        let mut i = 0;
        while i < n && intervals[i][1] < l {
            res.push(intervals[i].to_owned());
            i += 1;
        }
        while i < n && intervals[i][0] <= r {
            l = l.min(intervals[i][0]);
            r = r.max(intervals[i][1]);
            i += 1;
        }
        res.push(vec![l, r]);
        res.extend(intervals[i..].to_owned().into_iter());
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let intervals: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let new_interval: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::insert(intervals, new_interval).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

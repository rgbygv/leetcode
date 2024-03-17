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
    pub fn insert(mut intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let n = intervals.len();
        if n == 0 || new_interval[0] > intervals[n - 1][1] {
            intervals.push(new_interval);
            return intervals;
        }
        let (mut l, mut r) = (new_interval[0], new_interval[1]);
        if r < intervals[0][0] {
            intervals.insert(0, new_interval);
            return intervals;
        }
        let mut res = vec![];
        let mut i = 0;
        while i < n {
            let (x, y) = (intervals[i][0], intervals[i][1]);
            if y < l {
                res.push(vec![x, y]);
            } else if r < x {
                res.push(vec![l, r]);
				res.extend(intervals[i..].to_owned().into_iter());
                break;
            } else {
                l = l.min(x);
                r = r.max(y);
                while i < n && intervals[i][0] <= r {
                    r = r.max(intervals[i][1]);
                    i += 1;
                }
                res.push(vec![l, r]);
                res.extend(intervals[i..].to_owned().into_iter());
                break;
            }
            i += 1;
        }
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

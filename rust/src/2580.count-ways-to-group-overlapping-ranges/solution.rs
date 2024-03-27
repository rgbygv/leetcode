// Created by Jones at 2024/03/27 14:08
// leetgo: 1.4.3
// https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_ways(ranges: Vec<Vec<i32>>) -> i32 {
        let mut a = ranges;
        let m = 1e9 as i32 + 7;

        a.sort_unstable_by_key(|e| e[0]);

        let mut i = 0;
        let n = a.len();
        let mut res = 1;
        while i < n {
            let mut r = a[i][1];
            let mut j = i + 1;
            while j < n && a[j][0] <= r {
                r = r.max(a[j][1]);
                j += 1
            }
            // println!("{:?}", &a[i..j]);
            res = res * 2 % m;
            i = j
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ranges: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::count_ways(ranges).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

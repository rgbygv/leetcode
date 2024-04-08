// Created by Jones at 2024/04/08 13:34
// leetgo: 1.4.5
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut cnt = vec![0; 2];

        for x in students {
            cnt[x as usize] += 1;
        }

        let n = sandwiches.len();

        for (i, x) in sandwiches.into_iter().enumerate() {
            cnt[x as usize] -= 1;
            if cnt[x as usize] < 0 {
                return (n - i) as _;
            }
        }
        0
    }
}

// @lc code=end

fn main() -> Result<()> {
    let students: Vec<i32> = deserialize(&read_line()?)?;
    let sandwiches: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::count_students(students, sandwiches).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

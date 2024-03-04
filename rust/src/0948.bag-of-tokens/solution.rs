// Created by Jones at 2024/03/04 13:43
// leetgo: 1.4.1
// https://leetcode.com/problems/bag-of-tokens/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn bag_of_tokens_score(tokens: Vec<i32>, power: i32) -> i32 {
        if tokens.is_empty() {
            return 0;
        }
        let mut a = tokens;
        let mut power = power;
        a.sort_unstable();

        let n = a.len();
        let (mut left, mut right) = (0, n - 1);

        let mut res = 0;
        while left <= right {
            while left <= right && power >= a[left] {
                res += 1;
                power -= a[left];
                left += 1;
            }
            if left >= right {
                break;
            }
            if res > 0 {
                res -= 1;
                power += a[right];
                right -= 1;
            } else {
                break;
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let tokens: Vec<i32> = deserialize(&read_line()?)?;
    let power: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::bag_of_tokens_score(tokens, power).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

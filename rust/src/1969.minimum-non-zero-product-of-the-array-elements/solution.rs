// Created by Jones at 2024/03/20 00:18
// leetgo: 1.4.2
// https://leetcode.cn/problems/minimum-non-zero-product-of-the-array-elements/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

const MOD: i64 = 1e9 as i64 + 7;
pub fn quick_pow(mut a: i64, mut n: usize) -> i64 {
    a %= MOD;
    let mut x = a;
    let mut res = 1;
    while n > 0 {
        if n & 1 == 1 {
            res = res * x % MOD;
        }
        x = x * x % MOD;
        n >>= 1;
    }
    res as _
}
impl Solution {
    pub fn min_non_zero_product(p: i32) -> i32 {
        // the total number of 0, 1 at each pos will don't change
        // so we should divide the to small

        // (pow(2, p)-1) * pow((pow(2,p)-2), pow(2,p-1)-1)

        let p = p as usize;
        let tmp: i64 = (1 << p) - 1;
        (tmp % MOD * quick_pow(tmp - 1, (tmp >> 1) as usize) % MOD) as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let p: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_non_zero_product(p).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

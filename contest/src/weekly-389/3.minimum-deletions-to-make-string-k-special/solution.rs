// Created by Jones at 2024/03/17 21:45
// leetgo: 1.4.2
// https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/
// https://leetcode.cn/contest/weekly-contest-389/problems/minimum-deletions-to-make-string-k-special/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_deletions(word: String, k: i32) -> i32 {
        let mut cnt = vec![0; 26];
        let n = word.len();
        let k = k as usize;
        if k >= n {
            return 0;
        }

        for ch in word.bytes() {
            cnt[ch as usize - b'a' as usize] += 1;
        }
        cnt.sort_unstable_by_key(|&x| Reverse(x));
        while *cnt.last().unwrap() == 0 {
            cnt.pop();
        }
        let mut res = n;
        for &x in &cnt {
            let mut cur = 0;
            for &y in &cnt {
                // x-k, x+k
                if y < x {
                    cur += y
                } else if y > x + k {
                    cur += y - (x + k)
                }
            }
            res = res.min(cur)
        }
        res as _

        // let mut res = n;
        // for l in 0..=n - k {
        //     let r = l + k; // cnt[i] should in [l, r], or be 0
        //     let mut cur = 0;
        //     for &x in &cnt {
        //         if x == 0 || (l <= x && x <= r) {
        //             continue;
        //         }
        //         if x > r {
        //             cur += x - r;
        //         } else {
        //             cur += x;
        //         }
        //     }
        //     res = res.min(cur)
        // }

        // res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let word: String = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_deletions(word, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

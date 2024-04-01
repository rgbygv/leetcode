// Created by Jones at 2024/04/01 11:28
// leetgo: 1.4.3
// https://leetcode.cn/problems/faulty-keyboard/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn final_string(s: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut res = vec![];
        let mut flg = false;

        for ch in s {
            if ch == 'i' {
                flg = !flg;
            } else {
                if flg {
                    flg = false;
                    res.reverse();
                }
                res.push(ch);
            }
        }
        if flg {
            res.reverse();
        }

        res.into_iter().collect()

        /* let (mut i, mut j) = (0, s.len() - 1);

               let mut flg = true;
               while i <= j {
                   if flg {
                       if s[j] != 'i' {
                           res.push(s[j]);
                       } else {
                           flg = false;
                       }
                       j -= 1;
                   } else {
                       if s[i] != 'i' {
                           res.push(s[i]);
                       } else {
                           flg = true;
                       }
                       i += 1;
                   }
               }
        */
        // res.into_iter().rev().collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: String = Solution::final_string(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

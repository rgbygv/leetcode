// Created by Jones at 2024/03/19 18:20
// leetgo: 1.4.2
// https://leetcode.cn/problems/find-the-shortest-superstring/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn shortest_superstring(words: Vec<String>) -> String {
        let words: Vec<Vec<char>> = words.into_iter().map(|s| s.chars().collect()).collect();

        let n = words.len();

        let mut same = vec![vec![0; n]; n];
        let calc = |i: usize, j: usize| -> usize {
            let (s1, s2) = (&words[i], &words[j]);
            let m = s1.len();
            let n = s2.len();
            for k in (1..m.min(n)).rev() {
                if s1[m - k..] == s2[..k] {
                    return m - k;
                }
            }
            0
        };
        // let mut total = 0;
        for i in 0..n {
            // total += words[i].len();
            for j in i + 1..n {
                same[i][j] = calc(i, j)
            }
        }

        todo!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let words: Vec<String> = deserialize(&read_line()?)?;
    let ans: String = Solution::shortest_superstring(words).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

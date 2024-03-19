// Created by Jones at 2024/03/19 15:48
// leetgo: 1.4.2
// https://leetcode.cn/problems/task-scheduler/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut cnt = vec![0; 26];

        for ch in tasks {
            cnt[ch as usize - b'A' as usize] += 1;
        }

        // let max = *cnt.iter().max().unwrap();
        // let rest = cnt.iter().filter(|&x| *x == max).count() as i32;

        // (max - 1) * (n + 1) + rest

        let mut q = BinaryHeap::new();

        for x in cnt {
            if x != 0 {
                q.push(x)
            }
        }
		let n = n + 1; 
        let mut res = 0;
        while !q.is_empty() {
            let mut tmp = vec![];
            for i in 0..n {
                if let Some(max) = q.pop() {
                    res += 1;
                    if max > 1 {
                        tmp.push(max - 1)
                    }
                } else {
                    if !tmp.is_empty() {
                        res += n - i;
                    }
                    break;
                }
            }

            for x in tmp {
                q.push(x)
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let tasks: Vec<char> = deserialize(&read_line()?)?;
    let n: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::least_interval(tasks, n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

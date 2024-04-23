// Created by Jones at 2024/04/23 11:50
// leetgo: 1.4.5
// https://leetcode.com/problems/minimum-height-trees/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_min_height_trees(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        // we can know the root should be `mid`
        if n == 1 {
            return vec![0];
        }
        let mut deg = vec![0; n as usize];
        let mut g = vec![vec![]; n as usize];
        for e in &edges {
            let (x, y) = (e[0] as usize, e[1] as usize);
            deg[x] += 1;
            deg[y] += 1;
            g[x].push(y);
            g[y].push(x);
        }
        let mut q = VecDeque::from_iter((0..n as usize).filter(|&i| deg[i] == 1));
        let mut cnt = n as usize;
        while cnt > 2 {
            // println!("{:?} {cnt}", q);
            let t = q.len();
            for _ in 0..t {
                let x = q.pop_front().unwrap();
                cnt -= 1;
                deg[x] = 0;
                for &y in &g[x] {
                    deg[y] -= 1;
                    if deg[y] == 1 {
                        q.push_back(y);
                        // cnt -= 1;
                    }
                }
            }
        }

        q.into_iter().map(|x| x as i32).collect::<Vec<i32>>()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let edges: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::find_min_height_trees(n, edges).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

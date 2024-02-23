// Created by Jones at 2024/02/23 13:10
// leetgo: 1.4.1
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::collections::*;
// use std::mem::swap;
impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let n = n as usize;
        let (src, dst) = (src as usize, dst as usize);
        let mut g = vec![vec![]; n];

        for e in flights {
            let (x, y, p) = (e[0] as usize, e[1] as usize, e[2]);
            g[x].push((y, p));
        }
        let k = k as usize + 1;
        let mut dist = vec![vec![i32::MAX; n]; k + 1];
        dist[0][src] = 0;
        let mut q = VecDeque::new();
        q.push_back(src);
        for i in 0..k {
            let tn = q.len();
            for _ in 0..tn {
                let x = q.pop_front().unwrap();
                for &(y, p) in &g[x] {
                    if dist[i][x] != i32::MAX && dist[i][x] + p < dist[i + 1][y] {
                        dist[i + 1][y] = dist[i][x] + p;
                        q.push_back(y)
                    }
                }
            }
            for x in 0..n {
                dist[i + 1][x] = dist[i + 1][x].min(dist[i][x]);
            }
        }
        if dist[k][dst] == i32::MAX {
            -1
        } else {
            dist[k][dst]
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let flights: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let src: i32 = deserialize(&read_line()?)?;
    let dst: i32 = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_cheapest_price(n, flights, src, dst, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/03/22 11:16
// leetgo: 1.4.3
// https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_visited_cells(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());

        /*
        f[i][j] = min(f[i][k] for k in j+1..=grid[i][j] + j)
                | min(f[k][j] for k in i+1..=grid[i][j] + i)
        */

        let mut min = i32::MAX;
        let mut f: Vec<Vec<(i32, usize)>> = vec![vec![]; n];
        let mut row: Vec<(i32, usize)> = vec![];
        for i in (0..m).rev() {
            row.clear();
            for j in (0..n).rev() {
                min = if i < m - 1 || j < n - 1 { i32::MAX } else { 1 };
                let x = grid[i][j] as usize;
                if x > 0 {
                    // find below
                    let k = f[j].partition_point(|e| e.1 > x + i);
                    if k < f[j].len() {
                        min = f[j][k].0 + 1;
                    }
                    // find right
                    let k = row.partition_point(|e| e.1 > x + j);
                    if k < row.len() {
                        min = min.min(row[k].0 + 1);
                    }
                }

                let step = min;
                if step < i32::MAX {
                    while !row.is_empty() && row.last().unwrap().0 >= step {
                        row.pop();
                    }
                    row.push((step, j));
                    while !f[j].is_empty() && f[j].last().unwrap().0 >= step {
                        f[j].pop();
                    }
                    f[j].push((step, i));
                }
            }
        }
        if min == i32::MAX {
            -1
        } else {
            min
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_visited_cells(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

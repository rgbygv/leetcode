// Created by Jones at 2024/04/04 11:06
// leetgo: 1.4.3
// https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn get_ancestors(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut g = vec![vec![]; n];

        for e in edges {
            let (x, y) = (e[0] as usize, e[1] as usize);
            g[x].push(y)
        }

        let mut res = vec![HashSet::with_capacity(n); n];

        fn dfs(x: usize, fa: usize, g: &Vec<Vec<usize>>, res: &mut Vec<HashSet<i32>>) {
            for &y in &g[x] {
                res[y].insert(fa as i32);
                dfs(y, fa, g, res)
            }
        }

        for x in 0..n {
            dfs(x, x, &g, &mut res)
        }
        let mut res: Vec<Vec<i32>> = res.into_iter().map(|v| v.into_iter().collect()).collect();
        for i in 0..n {
            res[i].sort_unstable()
        }
        res
        // let mut deg = vec![0; n];
        // let mut g = vec![vec![]; n];

        // for e in &edges {
        //     let (x, y) = (e[0] as usize, e[1] as usize);
        //     g[y].push(x); // build rev gragh
        //     deg[x] += 1;
        // }
        // let mut f = vec![HashSet::with_capacity(n); n];

        // fn dfs(x:usize, g: &Vec<Vec<usize>>, f: &mut Vec<HashSet<usize>>, deg: &mut Vec<i32>) {
        // 	for &y in &g[x]{
        // 		f[x].insert(y);
        // 		deg[y] -= 1;
        // 		if deg[y] == 0{
        // 			dfs(y, g, f, deg);
        // 		}
        // 	}

        // 	todo!()
        // }

        // todo!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let edges: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::get_ancestors(n, edges).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

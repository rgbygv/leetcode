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
        let mut rg = vec![vec![]; n]; // reverse graph

        for e in &edges {
            let (x, y) = (e[0] as usize, e[1] as usize);
            rg[y].push(x); // build rev gragh
        }
        let mut f = vec![HashSet::with_capacity(n); n];
        let mut cache = HashMap::new();

        fn dfs(
            x: usize,
            rg: &Vec<Vec<usize>>,
            f: &mut Vec<HashSet<usize>>,
            cache: &mut HashMap<usize, HashSet<usize>>,
        ) -> HashSet<usize> {
            if cache.contains_key(&x) {
                return cache.get(&x).unwrap().to_owned();
            }
            for &y in &rg[x] {
                f[x].insert(y);
                for fa in dfs(y, rg, f, cache) {
                    f[x].insert(fa);
                }
            }
            cache.insert(x, f[x].clone());
            f[x].clone()
        }

        for x in 0..n {
            dfs(x, &rg, &mut f, &mut cache);
        }

        let mut res = vec![];

        for x in 0..n {
            let mut cur: Vec<i32> = f[x].iter().map(|&x| x as i32).collect();
            cur.sort_unstable();
            res.push(cur)
        }
        res
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

// Created by Jones at 2024/02/25 12:54
// leetgo: 1.4.1
// https://leetcode.com/problems/greatest-common-divisor-traversal/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

#[derive(Default)]
pub struct UnionFind {
    fa: Vec<usize>,
    rank: Vec<i32>,
    comp: usize,
}
impl UnionFind {
    pub fn new(n: usize) -> Self {
        Self {
            fa: (0..n).collect(),
            rank: vec![1; n],
            comp: n,
        }
    }

    pub fn find(&mut self, x: usize) -> usize {
        if self.fa[x] != x {
            self.fa[x] = self.find(self.fa[x])
        }
        self.fa[x]
    }

    pub fn union(&mut self, x: usize, y: usize) -> bool {
        let (mut fx, mut fy) = (self.find(x), self.find(y));
        if fx == fy {
            return false;
        }

        if self.rank[fx] < self.rank[fy] {
            swap(&mut fx, &mut fy);
        }
        self.fa[fy] = fx;
        self.rank[fx] += self.rank[fy];
        self.comp -= 1;
        true
    }
}

pub fn gcd(x: i32, y: i32) -> i32 {
    if y == 0 {
        return x;
    }
    gcd(y, x % y)
}

impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        if nums.len() == 1 {
            return true;
        }
        let a = nums.into_iter().collect::<HashSet<_>>();
        let mut a = a.into_iter().collect::<Vec<_>>();
        let n = a.len();
        a.sort_unstable();
        if a[0] == 1 {
            return false;
        }
        let m = *a.last().unwrap() as usize + 1;
        let mut g = vec![vec![]; m];
        for e in a.iter().enumerate() {
            let mut x = *e.1 as usize;
            let y = e.0;
            let mut d = 2;
            while d * d <= x {
                if x % d == 0 {
                    g[d].push(y);
                    while x % d == 0 {
                        x /= d;
                    }
                }
                d += 1;
            }
            if x > 1 {
                g[x].push(y);
            }
        }

        let mut uf = UnionFind::new(n);

        for v in g {
            for w in v.windows(2) {
                uf.union(w[0], w[1]);
            }
        }

        uf.comp == 1
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: bool = Solution::can_traverse_all_pairs(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/04/27 13:04
// leetgo: 1.4.5
// https://leetcode.com/problems/freedom-trail/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_rotate_steps(ring: String, key: String) -> i32 {
        // - `1 <= ring.length, key.length <= 100`
        // - `ring` and `key` consist of only lower case English letters.
        // - It is guaranteed that `key` could always be spelled by rotating `ring`.
        //
        let mut mp = HashMap::new();

        for (i, ch) in ring.char_indices() {
            mp.entry(ch).or_insert(vec![]).push(i);
        }
        // need a cache
        #[allow(dead_code)]
        fn dfs(
            i: usize,
            j: usize,
            s: &Vec<char>,
            target: &Vec<char>,
            mp: &HashMap<char, Vec<usize>>,
        ) -> i32 {
            // we now in ring[i], and need to find key[j]
            if j == target.len() {
                return 0;
            }

            let mut res = 1e9 as i32;
            for &idx in mp.get(&target[j]).unwrap() {
                let step = if idx <= i {
                    (i - idx).min(idx + s.len() - i)
                } else {
                    (idx - i).min(i + s.len() - idx)
                };
                res = res.min(step as i32 + dfs(idx, j + 1, s, target, mp))
            }
            res
        }

        let (m, n) = (ring.len(), key.len());
        let (s, target) = (
            ring.chars().collect::<Vec<char>>(),
            key.chars().collect::<Vec<char>>(),
        );

        let inf = 1e9 as i32;
        let mut f = vec![vec![inf; n + 1]; m];
        for i in 0..m {
            f[i][n] = 0
        }
        for j in (0..n).rev() {
            for i in (0..m).rev() {
                let mut res = inf;
                for &idx in mp.get(&target[j]).unwrap() {
                    let step = if idx <= i {
                        (i - idx).min(idx + s.len() - i)
                    } else {
                        (idx - i).min(i + s.len() - idx)
                    };
                    res = res.min(step as i32 + f[idx][j + 1])
                }
                f[i][j] = res;
            }
        }

        f[0][0] + n as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ring: String = deserialize(&read_line()?)?;
    let key: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_rotate_steps(ring, key).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

// Created by Jones at 2024/04/06 08:19
// leetgo: 1.4.5
// https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

struct TreeAncestor {
    pp: Vec<Vec<i32>>,
    m: usize,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TreeAncestor {
    fn new(n: i32, parent: Vec<i32>) -> Self {
        let n = n as usize;
        let m = (n as f64).log2() as usize + 1;

        let mut pp = vec![vec![-1; m]; n];
        for (i, &fa) in parent.iter().enumerate() {
            pp[i][0] = fa;
        }
        for x in 0..n {
            for i in 1..m {
                let p = pp[x][i - 1];
                if p != -1 {
                    pp[x][i] = pp[p as usize][i - 1];
                }
            }
        }

        // println!("{:?}", pp);
        Self { pp, m }
    }

    fn get_kth_ancestor(&self, node: i32, mut k: i32) -> i32 {
        let mut x = node as usize;
        k -= 1;

        for i in (0..self.m).rev() {
            if k >> i & 1 == 1 {
                let y = self.pp[x][i];
                if y == -1 {
                    return -1;
                }
                x = y as usize;
            }
        }
		// println!("{x}");
        self.pp[x][0]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    let constructor_params = split_array(&params[0])?;
    let n: i32 = deserialize(&constructor_params[0])?;
    let parent: Vec<i32> = deserialize(&constructor_params[1])?;
    #[allow(unused_mut)]
    let mut obj = TreeAncestor::new(n, parent);

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "getKthAncestor" => {
                let method_params = split_array(&params[i])?;
                let node: i32 = deserialize(&method_params[0])?;
                let k: i32 = deserialize(&method_params[1])?;
                let ans: i32 = obj.get_kth_ancestor(node, k).into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}

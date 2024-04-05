// Created by Jones at 2024/04/05 15:40
// leetgo: 1.4.5
// https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0;

        fn dfs(
            root: Option<Rc<RefCell<TreeNode>>>,
            mut max: Option<i32>,
            mut min: Option<i32>,
            res: &mut i32,
        ) {
            if let Some(r) = root {
                let mut r = r.borrow_mut();
                if let (Some(max), Some(min)) = (max.as_mut(), min.as_mut()) {
                    *res = (*res).max(*max - r.val).max(r.val - *min);
                    *max = (*max).max(r.val);
                    *min = (*min).min(r.val);
                } else {
                    max = Some(r.val);
                    min = Some(r.val);
                }
                dfs(r.left.take(), max, min, res);
                dfs(r.right.take(), max, min, res)
            }
        }

        dfs(root, None, None, &mut res);

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_ancestor_diff(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

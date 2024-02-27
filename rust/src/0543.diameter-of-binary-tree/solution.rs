// Created by Jones at 2024/02/27 13:27
// leetgo: 1.4.1
// https://leetcode.com/problems/diameter-of-binary-tree/

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
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(root: Option<Rc<RefCell<TreeNode>>>, res: &mut i32) -> i32 {
            if let Some(root) = root {
                let mut root = root.borrow_mut();
                let left = dfs(root.left.take(), res);
                let right = dfs(root.right.take(), res);
                *res = (left + right).max(*res);
                left.max(right) + 1
            } else {
                0
            }
        }
        let mut res = 0;
        dfs(root, &mut res);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::diameter_of_binary_tree(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

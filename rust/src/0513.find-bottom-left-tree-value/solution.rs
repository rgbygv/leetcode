// Created by Jones at 2024/02/28 12:05
// leetgo: 1.4.1
// https://leetcode.com/problems/find-bottom-left-tree-value/

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
    pub fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut height = vec![];

        fn dfs(root: Option<Rc<RefCell<TreeNode>>>, h: usize, height: &mut Vec<i32>) {
            if let Some(root) = root {
                let mut root = root.borrow_mut();
                // first meet the leftmost node
                if height.len() < h {
                    height.push(root.val);
                }
                dfs(root.left.take(), h + 1, height);
                dfs(root.right.take(), h + 1, height);
            }
        }

        dfs(root, 1, &mut height);
        *height.last().unwrap()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_bottom_left_value(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

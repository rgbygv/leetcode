// Created by Jones at 2024/02/26 12:16
// leetgo: 1.4.1
// https://leetcode.com/problems/same-tree/

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
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        if p.is_none() && q.is_none() {
            return true;
        } else if p.is_none() || q.is_none() {
            return false;
        }
        if let (Some(p), Some(q)) = (p, q) {
            let mut p = p.borrow_mut();
            let mut q = q.borrow_mut();
            p.val == q.val
                && Solution::is_same_tree(p.left.take(), q.left.take())
                && Solution::is_same_tree(p.right.take(), q.right.take())
        } else {
            false
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let p: BinaryTree = deserialize(&read_line()?)?;
    let q: BinaryTree = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_same_tree(p.into(), q.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

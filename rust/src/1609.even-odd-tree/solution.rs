// Created by Jones at 2024/02/29 14:43
// leetgo: 1.4.1
// https://leetcode.com/problems/even-odd-tree/

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
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut q = VecDeque::new();
        q.push_back(root);
        let mut flg = 1; // left -> right
        while !q.is_empty() {
            let n = q.len();
            let mut last: Option<i32> = None;
            for _ in 0..n {
                let root = q.pop_front().unwrap();
                if let Some(root) = root {
                    let mut root = root.borrow_mut();
                    if (root.val & 1 == 1) != (flg == 1) {
                        return false;
                    }
                    if let Some(l) = last {
                        if flg * (root.val - l) > 0 {
                            last = Some(root.val);
                        } else {
                            return false;
                        }
                    } else {
                        last = Some(root.val);
                    }
                    for child in [root.left.take(), root.right.take()] {
                        q.push_back(child);
                    }
                }
            }
            flg *= -1
        }
        true
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_even_odd_tree(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

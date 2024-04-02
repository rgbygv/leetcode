// Created by Jones at 2024/04/02 12:56
// leetgo: 1.4.3
// https://leetcode.cn/problems/all-possible-full-binary-trees/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

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
    pub fn all_possible_fbt(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        fn new() -> Option<Rc<RefCell<TreeNode>>> {
            Some(Rc::new(RefCell::new(TreeNode::new(0))))
        }
        if n & 1 == 0 {
            return vec![];
        }
        fn dfs(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
            if n == 1 {
                return vec![new()];
            }
            let mut res = vec![];
            for left in (1..n).step_by(2) {
                let right = n - 1 - left;
                for left in &dfs(left) {
                    for right in &dfs(right) {
                        let mut root = new();
                        root.as_mut().unwrap().borrow_mut().left = left.clone();
                        root.as_mut().unwrap().borrow_mut().right = right.clone();
                        res.push(root.to_owned());
                    }
                }
            }
            res
        }

        dfs(n)
    }
}

// @lc code=end

fn main() -> Result<()> {
    // let n: i32 = deserialize(&read_line()?)?;
    // let ans: Vec<BinaryTree> = Solution::all_possible_fbt(n).into();

    // println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

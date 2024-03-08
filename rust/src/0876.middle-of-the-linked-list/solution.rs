// Created by Jones at 2024/03/07 19:53
// leetgo: 1.4.1
// https://leetcode.cn/problems/middle-of-the-linked-list/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
// use std::collections::*;
use std::mem::swap;

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut fast = head.clone();
        let mut slow = head.clone();

        while fast.is_some() && fast.as_ref().unwrap().next.is_some() {
            fast = fast.unwrap().next.unwrap().next;
            slow = slow.unwrap().next;
        }

        slow
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::middle_node(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

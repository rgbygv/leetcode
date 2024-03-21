// Created by Jones at 2024/03/21 12:07
// leetgo: 1.4.3
// https://leetcode.com/problems/reverse-linked-list/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
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
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return head;
        }
        let mut p = None;

        // 1 -> 2 -> 3
        // p <- 1 <- 2 <- 3
        let mut head = head;
        while head.is_some() {
            let nxt = head.as_mut().unwrap().next.take();
            head.as_mut().unwrap().next = p;
            p = head;
            head = nxt;
            // head = nxt;
        }

        p
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::reverse_list(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

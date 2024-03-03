// Created by Jones at 2024/03/03 14:02
// leetgo: 1.4.1
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
    pub fn remove_nth_from_end(mut head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut size = 0;
        let mut p = head.clone();
        // count size
        while let Some(cur) = p {
            size += 1;
            p = cur.next;
        }

        if size == n {
            return head.unwrap().next;
        }
        let mut p = head.as_mut();

        for _ in 0..(size - n - 1) {
            p = p.unwrap().as_mut().next.as_mut();
        }

        // bad code
        let nxt = p.as_ref().unwrap().next.as_ref().unwrap().next.clone();

        p.unwrap().next = nxt;

        head
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let n: i32 = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::remove_nth_from_end(head.into(), n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

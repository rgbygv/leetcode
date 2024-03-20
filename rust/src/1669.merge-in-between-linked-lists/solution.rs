// Created by Jones at 2024/03/20 12:58
// leetgo: 1.4.2
// https://leetcode.cn/problems/merge-in-between-linked-lists/

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
    pub fn merge_in_between(
        mut list1: Option<Box<ListNode>>,
        a: i32,
        b: i32,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut p = list1.as_mut();
        // find the tail
        for _ in 0..b {
            p = p.unwrap().next.as_mut();
        }
        let tail = p.as_mut().unwrap().next.take();
        // find the head
        let mut q = list1.as_mut();
        for _ in 0..a - 1 {
            q = q.unwrap().next.as_mut();
        }

        // change pointer
        q.as_mut().unwrap().next = list2;
        while q.as_ref().unwrap().next.is_some() {
            q = q.unwrap().next.as_mut();
        }
        q.as_mut().unwrap().next = tail;
        list1
    }
}

// @lc code=end

// Warning: this is a manual question, the generated test code may be incorrect.
fn main() -> Result<()> {
    let list1: LinkedList = deserialize(&read_line()?)?;
    let a: i32 = deserialize(&read_line()?)?;
    let b: i32 = deserialize(&read_line()?)?;
    let list2: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::merge_in_between(list1.into(), a, b, list2.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

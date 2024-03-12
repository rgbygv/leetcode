// Created by Jones at 2024/03/12 12:11
// leetgo: 1.4.2
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::HashMap;
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
    pub fn remove_zero_sum_sublists(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let dummy = Box::new(ListNode { val: 0, next: head });
        let mut map = HashMap::new();
        map.insert(0, dummy.as_ref());

        let mut s = 0;
        let mut p = dummy.next.as_ref();
        while let Some(node) = p {
            s += node.val;
            p = node.next.as_ref();
            map.insert(s, node.as_ref());
        }

        s = 0;

        let mut res = Box::new(ListNode { val: 0, next: None });
        let mut p = Some(&mut res);
        while let Some(node) = p {
            s += node.val;
            if let Some(pre) = map.get(&s) {
                node.next = match pre.next.as_ref() {
                    Some(next) => Some(Box::new(ListNode {
                        val: next.val,
                        next: None,
                    })),
                    _ => None,
                }
            }
            p = node.next.as_mut();
        }
        res.next
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::remove_zero_sum_sublists(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

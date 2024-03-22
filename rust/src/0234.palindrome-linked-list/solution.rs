// Created by Jones at 2024/03/22 13:01
// leetgo: 1.4.3
// https://leetcode.com/problems/palindrome-linked-list/

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
    pub fn is_palindrome(mut head: Option<Box<ListNode>>) -> bool {
        if head.is_none() {
            return true;
        }
        // 1 -> 2 -> 3 -> 4

        // find the mid
        let mut fast = head.as_ref();
        let mut slow = head.as_ref();

        while fast.is_some() && fast.unwrap().next.is_some() {
            fast = fast.unwrap().next.as_ref().unwrap().next.as_ref();
            slow = slow.unwrap().next.as_ref();
        }
        // Only have 1 node
        if fast == head.as_ref() {
            return true;
        }

        let mut right_half = slow.take().cloned();
        right_half = Self::reverse_list(right_half);

        while right_half.is_some() {
            if head.as_ref().unwrap().val != right_half.as_ref().unwrap().val {
                return false;
            }
            head = head.unwrap().next;
            right_half = right_half.unwrap().next;
        }

        true
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_palindrome(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

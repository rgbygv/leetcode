// Created by Jones at 2024/03/26 11:52
// leetgo: 1.4.3
// https://leetcode.com/problems/first-missing-positive/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        // HashSet and check O(n) + O(n)
        // Sort O(nlogn) + O(1)
        // Binary Search O(nlogn) + O(1)
        // Quick Select O(n) + O(1) ???
        //

        let n = nums.len();

        for i in 0..n {
            if nums[i] < 1 || nums[i] > n as i32 || nums[i] == i as i32 + 1 {
                continue;
            }
            let mut i = i;
            let mut x = nums[i] as usize;

            loop {
                // println!("{i} {x} {:?}", nums);
                let j = nums[x - 1];
                nums[i] = 0;
                nums[x - 1] = x as i32;
                if j == x as i32 || j < 1 || j > n as i32 {
                    break;
                }
                x = j as usize;
                i = j as usize - 1;
            }
        }
        // println!("{:?}", nums);

        if nums[0] != 1 {
            return 1;
        }
        for i in 0..n {
            if nums[i] != i as i32 + 1 {
                return nums[i - 1] + 1;
            }
        }

        n as i32 + 1

        // fn quick_select(nums: &mut Vec<i32>, l: usize, r: usize) -> usize {
        //     if l == r {
        //         return l;
        //     }

        //     let (mut i, mut j) = (l, r);
        //     while i < j {
        //         while i < j && nums[i] <= nums[l] {
        //             i += 1;
        //         }
        //         if i == r {
        //             break;
        //         }
        //         while j > i && nums[j] > nums[l] {
        //             j -= 1;
        //         }

        //         (nums[i], nums[j]) = (nums[j], nums[i]);
        //         i += 1;
        //         j -= 1;
        //     }

        //     (nums[l], nums[j]) = (nums[j], nums[l]);

        //     // for nums[i], there're i + 1 <= nums[i]
        // }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::first_missing_positive(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

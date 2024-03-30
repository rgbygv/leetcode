// Created by Jones at 2024/03/30 11:01
// leetgo: 1.4.3
// https://leetcode.com/problems/subarrays-with-k-different-integers/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        const N: usize = 2e4 as usize + 1;
        let mut cnt = vec![0; N];
        let mut diff = 0;
        let mut res = 0;
        let mut l = 0;
        let mut mid = 0;

        for (r, &x) in nums.iter().enumerate() {
            let x = x as usize;
            if cnt[x] == 0 {
                diff += 1;
            }
            cnt[x] += 1;
            while diff > k {
                let x = nums[l] as usize;
                if l >= mid {
                    cnt[x] -= 1;
                    if cnt[x] == 0 {
                        diff -= 1;
                    }
                }
                l += 1;
            }

            if diff == k {
                mid = mid.max(l);
                // find the mid where [l..mid, r] is valid
                while mid < r {
                    let x = nums[mid] as usize;
                    if cnt[x] > 1 {
                        cnt[x] -= 1;
                        mid += 1;
                    } else {
                        break;
                    }
                }
                // println!("{}, {}, {}", l, mid, r);
                res += mid - l + 1
            }
        }

        res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::subarrays_with_k_distinct(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

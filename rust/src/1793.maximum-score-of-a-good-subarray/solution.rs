// Created by Jones at 2024/03/19 15:33
// leetgo: 1.4.2
// https://leetcode.cn/problems/maximum-score-of-a-good-subarray/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::mem::swap;

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;

        // find the range of nums[i] is minimal
        let mut left = vec![0; n];
        let mut right = vec![n - 1; n];

        let mut st = vec![];
        for (i, &x) in nums.iter().enumerate() {
            while let Some(j) = st.pop() {
                if x < nums[j] {
                    right[j] = i - 1;
                } else {
                    st.push(j);
                    break;
                }
            }
            if let Some(j) = st.last() {
                left[i] = *j + 1;
            }
            st.push(i)
        }

        let mut res = 0;
        for i in 0..n {
            let (l, r) = (left[i], right[i]);
            if l <= k && k <= r {
                res = res.max(nums[i] * (r - l + 1) as i32)
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_score(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

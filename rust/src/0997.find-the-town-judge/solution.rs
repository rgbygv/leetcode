// Created by Jones at 2024/02/22 13:30
// leetgo: 1.4.1
// https://leetcode.com/problems/find-the-town-judge/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
		let n = n as usize;
		let mut cnt = vec![0; n+1];
		let mut can = vec![true;n+1];
		for e in trust{
			can[e[0] as usize] = false;
			cnt[e[1] as usize] += 1;
		}
		for i in 1..=n{
			if can[i] && cnt[i] == n-1{
				return i as i32
			}
		}
		-1

        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let n: i32 = deserialize(&read_line()?)?;
	let trust: Vec<Vec<i32>> = deserialize(&read_line()?)?;
	let ans: i32 = Solution::find_judge(n, trust).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}

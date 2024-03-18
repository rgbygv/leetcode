// Created by Jones at 2024/03/18 13:59
// leetgo: 1.4.2
// https://leetcode.cn/problems/range-sum-query-immutable/

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

struct NumArray {
    prefix: Vec<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        let n = nums.len();
        let mut prefix = vec![0; n + 1];
        for (i, x) in nums.into_iter().enumerate() {
            prefix[i + 1] = prefix[i] + x
        }
        Self { prefix }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        self.prefix[right as usize + 1] - self.prefix[left as usize]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    let constructor_params = split_array(&params[0])?;
    let nums: Vec<i32> = deserialize(&constructor_params[0])?;
    // let nums_size: i32 = deserialize(&constructor_params[1])?;
    #[allow(unused_mut)]
    let mut obj = NumArray::new(nums);

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "sumRange" => {
                let method_params = split_array(&params[i])?;
                let left: i32 = deserialize(&method_params[0])?;
                let right: i32 = deserialize(&method_params[1])?;
                let ans: i32 = obj.sum_range(left, right).into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}

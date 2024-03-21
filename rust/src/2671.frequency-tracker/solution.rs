// Created by Jones at 2024/03/21 11:55
// leetgo: 1.4.3
// https://leetcode.cn/problems/frequency-tracker/

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

struct FrequencyTracker {
    cnt: Vec<usize>,
    freq: Vec<usize>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
const N: usize = 1e5 as usize + 1;
impl FrequencyTracker {
    fn new() -> Self {
        Self {
            cnt: vec![0; N],
            freq: vec![0; N],
        }
    }

    fn add(&mut self, number: i32) {
        let x = number as usize;
        if self.cnt[x] == 0 {
            self.cnt[x] = 1;
            self.freq[1] += 1;
        } else {
            self.freq[self.cnt[x]] -= 1;
            self.cnt[x] += 1;
            self.freq[self.cnt[x]] += 1;
        }
    }

    fn delete_one(&mut self, number: i32) {
        let x = number as usize;
        if self.cnt[x] > 0 {
            self.freq[self.cnt[x]] -= 1;
            self.cnt[x] -= 1;
            self.freq[self.cnt[x]] += 1;
        }
    }

    fn has_frequency(&self, frequency: i32) -> bool {
        self.freq[frequency as usize] > 0
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    #[allow(unused_mut)]
    let mut obj = FrequencyTracker::new();

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "add" => {
                let method_params = split_array(&params[i])?;
                let number: i32 = deserialize(&method_params[0])?;
                obj.add(number);
                output.push("null".to_string());
            }
            "deleteOne" => {
                let method_params = split_array(&params[i])?;
                let number: i32 = deserialize(&method_params[0])?;
                obj.delete_one(number);
                output.push("null".to_string());
            }
            "hasFrequency" => {
                let method_params = split_array(&params[i])?;
                let frequency: i32 = deserialize(&method_params[0])?;
                let ans: bool = obj.has_frequency(frequency).into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}

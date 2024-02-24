// Created by Jones at 2024/02/24 14:03
// leetgo: 1.4.1
// https://leetcode.com/problems/find-all-people-with-secret/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let _ = n;
        let mut a = meetings;
        a.sort_unstable_by_key(|e| e[2]);

        let mut f = HashSet::new();
        f.insert(0);
        f.insert(first_person as usize);

        let mut g = HashMap::new();
        let mut last = -1;
        for e in a {
            // print!("{e:?} {f:?}\n");
            let x = e[0] as usize;
            let y = e[1] as usize;
            let t = e[2];
            // deal with last group and create a new group
            if t != last {
                let mut q = VecDeque::new();
                // find start
                for x in g.keys() {
                    if f.contains(x) {
                        q.push_back(x);
                    }
                }

                while let Some(x) = q.pop_front() {
                    for y in g.get(&x).unwrap() {
                        if !f.contains(y) {
                            f.insert(*y);
                            q.push_back(y);
                        }
                    }
                }
                last = t;
                g.clear();
            }

            g.entry(x).or_insert(vec![]).push(y);
            g.entry(y).or_insert(vec![]).push(x);
        }
        let mut q = VecDeque::new();
        // find start
        for x in g.keys() {
            if f.contains(x) {
                q.push_back(x);
            }
        }

        while let Some(x) = q.pop_front() {
            for y in g.get(&x).unwrap() {
                if !f.contains(y) {
                    f.insert(*y);
                    q.push_back(y);
                }
            }
        }
        f.into_iter().map(|x| x as i32).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let meetings: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let first_person: i32 = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::find_all_people(n, meetings, first_person).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

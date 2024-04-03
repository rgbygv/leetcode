// Created by Jones at 2024/04/03 21:20
// leetgo: 1.4.3
// https://leetcode.com/problems/word-search/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let word: Vec<char> = word.chars().collect();

        fn dfs(
            board: &Vec<Vec<char>>,
            word: &Vec<char>,
            i: usize,
            x: usize,
            y: usize,
            mask: usize,
        ) -> bool {
            let m = board.len() as i32;
            let n = board[0].len() as i32;
            if board[x][y] == word[i] {
                if i == word.len() - 1 {
                    return true;
                }
                for d in [0, -1, 0, 1, 0].windows(2) {
                    let nx = x as i32 + d[0];
                    let ny = y as i32 + d[1];
                    if nx >= 0 && nx < m && ny >= 0 && ny < n {
                        let cur_bit = nx * n + ny;
                        if mask & (1 << cur_bit) != 0
                            && dfs(
                                board,
                                word,
                                i + 1,
                                nx as usize,
                                ny as usize,
                                mask ^ (1 << cur_bit),
                            )
                        {
                            return true;
                        }
                    }
                }
            }
            false
        }

        let m = board.len();
        let n = board[0].len();
        let base = (1 << (m * n)) - 1;
        for x in 0..m {
            for y in 0..n {
                if dfs(&board, &word, 0, x, y, base ^ (1 << (x * n + y))) {
                    return true;
                }
            }
        }
        false
    }
}

// @lc code=end

fn main() -> Result<()> {
    let board: Vec<Vec<char>> = deserialize(&read_line()?)?;
    let word: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::exist(board, word).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}

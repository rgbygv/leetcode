// Created by Jones at 2024/03/26 10:59
// leetgo: 1.4.3
// https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

struct Graph {

}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Graph {

    fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {

    }
    
    fn add_edge(&self, edge: Vec<i32>) {

    }
    
    fn shortest_path(&self, node1: i32, node2: i32) -> i32 {

    }
}

// @lc code=end

fn main() -> Result<()> {
	let ops: Vec<String> = deserialize(&read_line()?)?;
	let params = split_array(&read_line()?)?;
	let mut output = Vec::with_capacity(ops.len());
	output.push("null".to_string());

	let constructor_params = split_array(&params[0])?;
	let n: i32 = deserialize(&constructor_params[0])?;
	let edges: Vec<Vec<i32>> = deserialize(&constructor_params[1])?;
	#[allow(unused_mut)]
	let mut obj = Graph::new(n, edges);

	for i in 1..ops.len() {
		match ops[i].as_str() {
			"addEdge" => {
				let method_params = split_array(&params[i])?;
				let edge: Vec<i32> = deserialize(&method_params[0])?;
				obj.add_edge(edge);
				output.push("null".to_string());
			}
			"shortestPath" => {
				let method_params = split_array(&params[i])?;
				let node1: i32 = deserialize(&method_params[0])?;
				let node2: i32 = deserialize(&method_params[1])?;
				let ans: i32 = obj.shortest_path(node1, node2).into();
				output.push(serialize(ans)?);
			}
			_ => panic!("unknown op"),
		}
	}

	println!("\noutput: {}", join_array(output));
	Ok(())
}

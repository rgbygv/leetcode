// Created by Jones at 2024/04/07 11:13
// leetgo: 1.4.5
// https://leetcode.cn/problems/throne-inheritance/

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

#[derive(Default)]
struct ThroneInheritance {
    kings: HashMap<String, Vec<String>>,
    dead: HashSet<String>,
    king_name: String,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ThroneInheritance {
    fn new(king_name: String) -> Self {
        let mut kings = HashMap::new();
        kings.insert(king_name.to_owned(), vec![]);
        Self {
            kings,
            dead: HashSet::new(),
            king_name,
        }
    }

    fn birth(&mut self, parent_name: String, child_name: String) {
        if let Some(v) = self.kings.get_mut(&parent_name) {
            v.push(child_name.clone());
        }
        self.kings.insert(child_name, vec![]);
    }

    fn death(&mut self, name: String) {
        self.dead.insert(name);
    }

    fn get_inheritance_order(&self) -> Vec<String> {
        let mut res = vec![];

        let king = &self.king_name;
        fn dfs(
            res: &mut Vec<String>,
            king: &String,
            kings: &HashMap<String, Vec<String>>,
            dead: &HashSet<String>,
        ) {
            if !dead.contains(king) {
                res.push(king.to_owned())
            }
            if let Some(v) = kings.get(king) {
                for child in v {
                    dfs(res, child, kings, dead)
                }
            }
        }
        // let mut q = VecDeque::new();
        // q.push_back(king);
        // while let Some(king) = q.pop_front() {
        //     if !self.dead.contains(king) {
        //         res.push(king.to_owned())
        //     }
        //     if let Some(v) = self.kings.get(king) {
        //         for child in v {
        //             q.push_back(child);
        //         }
        //     }
        // }
        dfs(&mut res, king, &self.kings, &self.dead);
        // println!("{:?}\n{:?}\n{:?}", self.kings, self.dead, res);

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    let constructor_params = split_array(&params[0])?;
    let king_name: String = deserialize(&constructor_params[0])?;
    #[allow(unused_mut)]
    let mut obj = ThroneInheritance::new(king_name);

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "birth" => {
                let method_params = split_array(&params[i])?;
                let parent_name: String = deserialize(&method_params[0])?;
                let child_name: String = deserialize(&method_params[1])?;
                obj.birth(parent_name, child_name);
                output.push("null".to_string());
            }
            "death" => {
                let method_params = split_array(&params[i])?;
                let name: String = deserialize(&method_params[0])?;
                obj.death(name);
                output.push("null".to_string());
            }
            "getInheritanceOrder" => {
                let ans: Vec<String> = obj.get_inheritance_order().into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}

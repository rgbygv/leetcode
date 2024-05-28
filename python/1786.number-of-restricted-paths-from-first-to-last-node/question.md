# [1786. Number of Restricted Paths From First to Last Node][link] (Medium)

[link]: https://leetcode.cn/problems/number-of-restricted-paths-from-first-to-last-node/

There is an undirected weighted connected graph. You are given a positive integer `n` which denotes
that the graph has `n` nodes labeled from `1` to `n`, and an array `edges` where each `edges[i] =
[uᵢ, vᵢ, weightᵢ]` denotes that there is an edge between nodes `uᵢ` and `vᵢ` with weight equal to
`weightᵢ`.

A path from node `start` to node `end` is a sequence of nodes `[z₀, z₁,z₂, ..., zₖ]` such that `z₀
= start` and `zₖ = end` and there is an edge between `zᵢ` and `zᵢ₊₁` where `0 <= i <= k-1`.

The distance of a path is the sum of the weights on the edges of the path. Let
`distanceToLastNode(x)` denote the shortest distance of a path between node `n` and node `x`. A
**restricted path** is a path that also satisfies that `distanceToLastNode(zᵢ) >
distanceToLastNode(zᵢ₊₁)` where `0 <= i <= k-1`.

Return the number of restricted paths from node `1`to node `n`. Since that number may be too large,
return it **modulo** `10⁹ + 7`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/17/restricted_paths_ex1.png)

```
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue.
The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/17/restricted_paths_ex22.png)

```
Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue.
The only restricted path is 1 --> 3 --> 7.
```

**Constraints:**

- `1 <= n <= 2 * 10⁴`
- `n - 1 <= edges.length <= 4 * 10⁴`
- `edges[i].length == 3`
- `1 <= uᵢ, vᵢ <= n`
- `uᵢ != vᵢ`
- `1 <= weightᵢ <= 10⁵`
- There is at most one edge between any two nodes.
- There is at least one path between any two nodes.

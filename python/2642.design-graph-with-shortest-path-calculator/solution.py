# Created by Jones at 2023/11/11 19:49
# leetgo: dev
# https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, log2, perm, sqrt
from operator import xor
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = [[] for _ in range(n)]
        for x, y, c in edges:
            self.g[x].append((y, c))

    def addEdge(self, edge: List[int]) -> None:
        x, y, c = edge
        self.g[x].append((y, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [inf] * self.n
        dist[node1] = 0
        q = [(0, node1)]
        while q:
            d, x = heappop(q)
            for y, c in self.g[x]:
                if d + c < dist[y]:
                    dist[y] = d + c
                    heappush(q, (dist[y], y))

        res = dist[node2]
        if res == inf:
            return -1
        return res


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    edges: List[List[int]] = deserialize("List[List[int]]", constructor_params[1])
    obj = Graph(n, edges)

    for i in range(1, len(ops)):
        match ops[i]:
            case "addEdge":
                method_params = split_array(params[i])
                edge: List[int] = deserialize("List[int]", method_params[0])
                obj.addEdge(edge)
                output.append("null")
            case "shortestPath":
                method_params = split_array(params[i])
                node1: int = deserialize("int", method_params[0])
                node2: int = deserialize("int", method_params[1])
                ans = serialize(obj.shortestPath(node1, node2))
                output.append(ans)

    print("\noutput:", join_array(output))

# Created by Jones at 2024/07/01 10:18
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-path-quality-of-a-graph/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int
    ) -> int:
        """
        - `n == values.length`
        - `1 <= n <= 1000`
        - `0 <= values[i] <= 10⁸`
        - `0 <= edges.length <= 2000`
        - `edges[j].length == 3 `
        - `0 <= uⱼ < vⱼ <= n - 1`
        - `10 <= timeⱼ, maxTime <= 100`
        - All the pairs `[uⱼ, vⱼ]` are **unique**.
        - There are **at most four** edges connected to each node.
        - The graph may not be connected.
        """
        # at most 10 step,  10 nodes
        n = len(values)
        g = [[] for _ in range(n)]

        for x, y, t in edges:
            g[x].append((y, t))
            g[y].append((x, t))

        @cache
        def dfs(x: int, rest_time: int, mask: int):
            if rest_time < 0:
                return -1
            res = 0
            if x == 0:
                res = sum(v for i, v in enumerate(values) if mask >> i & 1)
            for y, t in g[x]:
                if (rt := rest_time - t) >= 0:
                    res = max(res, dfs(y, rt, mask | (1 << y)))

            return res

        return dfs(0, maxTime, 1)


# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    maxTime: int = deserialize("int", read_line())
    ans = Solution().maximalPathQuality(values, edges, maxTime)
    print("\noutput:", serialize(ans, "integer"))

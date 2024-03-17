# Created by Jones at 2024/03/17 12:45
# leetgo: 1.4.2
# https://leetcode.cn/problems/minimum-height-trees/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i, d in enumerate(deg) if d == 1]
        q = deque(q)
        while n > 2:
            t = len(q)
            n -= t
            for _ in range(t):
                x = q.popleft()
                deg[x] = 0  # tag as visited
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return list(q)

        # (first, second) highest of subtree
        # heights = [[-1, -1] for _ in range(n)]

        # def dfs(x, fa):
        #     fi = se = 1
        #     for y in g[x]:
        #         if y != fa:
        #             sub = dfs(y, x)
        #             if sub > fi:
        #                 fi, se = sub, fi
        #             elif sub > se:
        #                 se = sub

        #     heights[x] = [fi, se]
        #     return fi

        # h = dfs(0, -1)

        # def change_root(x, fa):
        #     for y in g[x]:
        #         if y == fa:
        #             continue


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMinHeightTrees(n, edges)
    print("\noutput:", serialize(ans, "integer[]"))

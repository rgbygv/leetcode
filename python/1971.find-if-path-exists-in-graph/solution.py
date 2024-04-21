# Created by Jones at 2024/04/21 13:11
# leetgo: 1.4.5
# https://leetcode.com/problems/find-if-path-exists-in-graph/

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
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        we can use UnionFind also.
        """
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        vis = [False] * n

        def dfs(x: int):
            """Traverse the edges of a point"""
            if x == destination:
                return True
            # don't visit a node twice
            if vis[x]:
                return
            vis[x] = True

            # Traverse edges
            for y in g[x]:
                if dfs(y):
                    return True
            return False

        return dfs(source)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    ans = Solution().validPath(n, edges, source, destination)
    print("\noutput:", serialize(ans, "boolean"))

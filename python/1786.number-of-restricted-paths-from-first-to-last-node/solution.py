# Created by Jones at 2024/05/28 14:49
# leetgo: 1.4.7
# https://leetcode.cn/problems/number-of-restricted-paths-from-first-to-last-node/

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
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7

        g = [[] for _ in range(n + 1)]

        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        # compute te shortest path to `n`
        dist = [inf] * (n + 1)
        dist[n] = 0
        q = [(0, n)]
        while q:
            d, x = heappop(q)
            for y, w in g[x]:
                if dist[y] > (new := d + w):
                    dist[y] = new
                    heappush(q, (new, y))

        @cache
        def dfs(x):
            if x == 1:
                return 1
            res = 0
            for y, _ in g[x]:
                if dist[1] >= dist[y] > dist[x]:
                    res += dfs(y)
            return res % mod

        res = dfs(n)
        dfs.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countRestrictedPaths(n, edges)
    print("\noutput:", serialize(ans, "integer"))

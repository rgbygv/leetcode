# Created by Jones at 2024/05/01 18:57
# leetgo: 1.4.5
# https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/

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
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        g = [[] for _ in range(n)]
        for i, (x, y) in enumerate(stones):
            for j in range(i):
                cx, cy = stones[j]
                if cx == x or cy == y:
                    g[j].append(i)
                    g[i].append(j)

        res = 0
        f = [False] * n  # visited

        def dfs(x):
            if f[x]:
                return 0
            res = 1
            f[x] = True
            for y in g[x]:
                res += dfs(y)
            return res

        # ic(g)
        for x in range(n):
            if f[x]:
                continue
            size = dfs(x)
            res += size - 1
        return res


# @lc code=end

if __name__ == "__main__":
    stones: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().removeStones(stones)
    print("\noutput:", serialize(ans, "integer"))

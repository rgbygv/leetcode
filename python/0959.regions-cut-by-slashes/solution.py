# Created by Jones at 2024/05/01 19:16
# leetgo: 1.4.5
# https://leetcode.cn/problems/regions-cut-by-slashes/

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
    def regionsBySlashes(self, grid: List[str]) -> int:
        g = []
        n = len(grid)
        """
        we expand "/" to 0 1
                         1
        but it have problem,

        we expand to 3 * 3
        """
        size = len(grid[0]) * 3

        for row in grid:
            expand = [[0] * size for _ in range(3)]
            idx = 0  # idx of expand
            j = 0
            while j < len(row):
                # ic(row, len(row), j, row[j])
                if row[j] == "/":
                    expand[0][idx + 2] = 1
                    expand[1][idx + 1] = 1
                    expand[2][idx] = 1
                elif row[j] == "\\":
                    expand[0][idx] = 1
                    expand[1][idx + 1] = 1
                    expand[2][idx + 2] = 1
                idx += 3
                j += 1
            g.extend(expand)

        m = len(g)
        n = len(g[0])

        res = 0

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if g[x][y] != 0:
                return
            g[x][y] = 1
            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                dfs(x + dx, y + dy)

        # ic("\n",g)
        for i in range(m):
            for j in range(n):
                if g[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[str] = deserialize("List[str]", read_line())
    ans = Solution().regionsBySlashes(grid)
    print("\noutput:", serialize(ans, "integer"))

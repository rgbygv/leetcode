# Created by Jones at 2024/05/07 12:48
# leetgo: 1.4.6
# https://leetcode.cn/problems/cherry-pickup-ii/

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
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        - `rows == grid.length`
        - `cols == grid[i].length`
        - `2 <= rows, cols <= 70`
        - `0 <= grid[i][j] <= 100`
        """
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j1: int, j2: int):
            """j1 < j2"""
            if i == m:
                return 0
            if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
                return -inf
            if j1 >= j2:
                return -inf
            res = 0
            for d1 in (-1, 0, 1):
                for d2 in (-1, 0, 1):
                    res = max(res, dfs(i + 1, j1 + d1, j2 + d2))
            return res + grid[i][j1] + grid[i][j2]

        return dfs(0, 0, n - 1)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cherryPickup(grid)
    print("\noutput:", serialize(ans, "integer"))

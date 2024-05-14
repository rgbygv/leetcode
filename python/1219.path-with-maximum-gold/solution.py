# Created by Jones at 2024/05/14 16:34
# leetgo: 1.4.7
# https://leetcode.com/problems/path-with-maximum-gold/

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
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        - `m == grid.length`
        - `n == grid[i].length`
        - `1 <= m, n <= 15`
        - `0 <= grid[i][j] <= 100`
        - There are at most **25** cells containing gold.
        """
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            v = grid[i][j]
            grid[i][j] = 0
            res = 0
            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                res = max(res, dfs(i + dx, j + dy))
            grid[i][j] = v
            return res + v

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getMaximumGold(grid)
    print("\noutput:", serialize(ans, "integer"))

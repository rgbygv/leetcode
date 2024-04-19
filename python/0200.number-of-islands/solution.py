# Created by Jones at 2024/04/19 13:32
# leetgo: 1.4.5
# https://leetcode.com/problems/number-of-islands/

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
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] != "1":
                return
            grid[i][j] = "2"  # tag as visited
            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                dfs(i + dx, j + dy)

        res = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == "1":
                    res += 1
                    dfs(i, j)
        return res


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().numIslands(grid)
    print("\noutput:", serialize(ans, "integer"))

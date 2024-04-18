# Created by Jones at 2024/04/18 10:24
# leetgo: 1.4.5
# https://leetcode.com/problems/island-perimeter/

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
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # res = 4 * size - 2 * adjust of cells
        size = 0
        cnt = 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            nonlocal size, cnt
            if grid[i][j] != 1:
                return
            size += 1
            grid[i][j] = 2  # tag as visited
            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                    cnt += 1
                    dfs(x, y)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    dfs(i, j)
                    print(size, cnt)
                    return 4 * size - cnt
        return 0


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().islandPerimeter(grid)
    print("\noutput:", serialize(ans, "integer"))

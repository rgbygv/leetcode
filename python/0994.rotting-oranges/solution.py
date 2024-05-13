# Created by Jones at 2024/05/13 14:08
# leetgo: 1.4.7
# https://leetcode.cn/problems/rotting-oranges/

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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - `m == grid.length`
        - `n == grid[i].length`
        - `1 <= m, n <= 10`
        - `grid[i][j]` is `0`, `1`, or `2`.
        """
        m, n = len(grid), len(grid[0])

        cnt = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 2:
                    q.append((i, j))
                elif x == 1:
                    cnt += 1

        if cnt == 0:
            return 0

        t = 0
        while q or cnt > 0:
            if cnt == 0:
                return t
            if not q:
                return -1
            t += 1
            nxt = []
            for x, y in q:
                for dx, dy in pairwise((0, 1, 0, -1, 0)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        cnt -= 1
                        nxt.append((nx, ny))
                        grid[nx][ny] = 2
            q = nxt


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().orangesRotting(grid)
    print("\noutput:", serialize(ans, "integer"))

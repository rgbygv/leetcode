# Created by Jones at 2023/11/22 10:54
# leetgo: dev
# https://leetcode.cn/problems/minimum-path-cost-in-a-grid/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        f = [[inf] * n for _ in range(m)]
        for j in range(n):
            f[0][j] = grid[0][j]

        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    x = grid[i - 1][k]
                    f[i][j] = min(f[i][j], f[i - 1][k] + moveCost[x][j])
                f[i][j] += grid[i][j]
        # print(f)

        return min(f[m - 1])


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    moveCost: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathCost(grid, moveCost)

    print("\noutput:", serialize(ans))

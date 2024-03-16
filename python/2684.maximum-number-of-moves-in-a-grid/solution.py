# Created by Jones at 2024/03/16 12:42
# leetgo: 1.4.2
# https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/

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
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        f = [0] * (m)
        res = 0
        for i in range(1, n):
            g = [0] * m
            for j in range(m):
                for k in range(j - 1, j + 2):
                    if (
                        0 <= k < m
                        and grid[k][i - 1] < grid[j][i]
                        and (f[k] != 0 or i == 1)
                    ):
                        g[j] = max(g[j], f[k] + 1)
            f = g
            res = max(res, max(f))
            if res == 0:
                return 0
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxMoves(grid)
    print("\noutput:", serialize(ans, "integer"))

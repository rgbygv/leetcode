# Created by Jones at 2024/05/13 14:14
# leetgo: 1.4.7
# https://leetcode.com/problems/score-after-flipping-matrix/

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
    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        - `m == grid.length`
        - `n == grid[i].length`
        - `1 <= m, n <= 20`
        - `grid[i][j]` is either `0` or `1`.
        """
        # if grid[i][0] is 0, we will reverse this row

        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0]:
                for j in range(n):
                    grid[i][j] ^= 1

        res = (1 << (n - 1)) * m  # fisrt row all is 1

        for j in range(1, n):
            s = sum(grid[i][j] == 1 for i in range(m))
            res += max(s, m - s) * (1 << (n - 1 - j))
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixScore(grid)
    print("\noutput:", serialize(ans, "integer"))

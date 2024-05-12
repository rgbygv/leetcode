# Created by Jones at 2024/05/12 18:20
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-difference-score-in-a-grid/
# https://leetcode.cn/contest/weekly-contest-397/problems/maximum-difference-score-in-a-grid/

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
    def maxScore(self, grid: List[List[int]]) -> int:
        """
        - `m == grid.length`
        - `n == grid[i].length`
        - `2 <= m, n <= 1000`
        - `4 <= m * n <= 10⁵`
        - `1 <= grid[i][j] <= 10⁵`
        """
        m, n = len(grid), len(grid[0])

        # f[i][j] = f[x][y] + grid[i][j] - grid[x][y]
        # so we find the max(f[x][y] - grid[x][y]) for x <= i and y <= j

        f = [[-inf] * (n + 1) for _ in range(m + 1)]
        g = [[-inf] * (n + 1) for _ in range(m + 1)]
        g[1][1] = -grid[0][0]

        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                if i == 1 and j == 1:
                    continue
                f[i][j] = x + max(g[i - 1][j], g[i][j - 1])
                g[i][j] = max(max(0, f[i][j]) - x, g[i - 1][j], g[i][j - 1])

        return max(max(row) for row in f)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxScore(grid)
    print("\noutput:", serialize(ans, "integer"))

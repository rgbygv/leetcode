# Created by Jones at 2024/05/06 12:31
# leetgo: 1.4.6
# https://leetcode.cn/problems/cherry-pickup/

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
        n = len(grid)

        @cache
        def dfs(k, x1, x2):
            if k == 2 * n - 1:
                return 0
            y1, y2 = k - x1, k - x2
            if x1 >= n or y1 >= n or x2 >= n or y2 >= n:
                return -inf
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -inf
            res = grid[x1][y1]
            if not (x1 == x2):
                res += grid[x2][y2]
            res += max(
                dfs(k + 1, x1, x2),
                dfs(k + 1, x1 + 1, x2),
                dfs(k + 1, x1, x2 + 1),
                dfs(k + 1, x1 + 1, x2 + 1),
            )

            return res

        res = dfs(0, 0, 0)
        dfs.cache_clear()
        if res == -inf:
            return 0
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cherryPickup(grid)
    print("\noutput:", serialize(ans, "integer"))

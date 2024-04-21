# Created by Jones at 2024/04/21 13:16
# leetgo: 1.4.5
# https://leetcode.cn/problems/minimum-number-of-operations-to-satisfy-conditions/
# https://leetcode.cn/contest/weekly-contest-394/problems/minimum-number-of-operations-to-satisfy-conditions/

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
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # if we can know the last row, we can know the grid

        cnt = [[0] * 10 for _ in range(n)]
        for _, row in enumerate(grid):
            for j, x in enumerate(row):
                cnt[j][x] += 1

        @cache
        def dfs(i: int, last: int = -1):
            if i == n:
                return 0
            res = inf
            for x in range(10):
                if last == -1 or x != last:
                    res = min(res, m - cnt[i][x] + dfs(i + 1, x))
                else:
                    res = min(res, m + dfs(i + 1, -1))
            return res

        return dfs(0, -1)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumOperations(grid)
    print("\noutput:", serialize(ans, "integer"))

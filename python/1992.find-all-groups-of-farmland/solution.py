# Created by Jones at 2024/04/20 14:11
# leetgo: 1.4.5
# https://leetcode.com/problems/find-all-groups-of-farmland/

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
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])

        res = []

        def dfs(i: int, j: int):
            """
            we start dfs from (i,j).
            problem assert group is rectangle, we only tag point as visited.
            if group is not assert is ractangle, this problem is more complex.
            """
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if land[i][j] != 1:
                return
            land[i][j] = 2
            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                dfs(i + dx, j + dy)

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    # find the bot
                    bot = i
                    while bot < m and land[bot][j] == 1:
                        bot += 1
                    # find the right
                    right = j
                    while right < n and land[i][right] == 1:
                        right += 1
                    res.append([i, j, bot - 1, right - 1])
                    dfs(i, j)

        return res


# @lc code=end

if __name__ == "__main__":
    land: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findFarmland(land)
    print("\noutput:", serialize(ans, "integer[][]"))

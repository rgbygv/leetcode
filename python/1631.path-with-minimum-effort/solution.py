# Created by Jones at 2023/12/11 20:18
# leetgo: dev
# https://leetcode.cn/problems/path-with-minimum-effort/

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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        l = 0
        r = int(1e6) + 1
        m = len(heights)
        n = len(heights[0])
        while l < r:
            mid = (l + r) >> 1

            def check(mid):
                vis = set()

                def dfs(x, y):
                    if x == m - 1 and y == n - 1:
                        return True
                    if (x, y) in vis:
                        return False
                    vis.add((x,y))
                    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < m
                            and 0 <= ny < n
                            and abs(heights[nx][ny] - heights[x][y]) <= mid
                        ):
                            if dfs(nx, ny):
                                return True
                    return False

                return dfs(0, 0)

            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    heights: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumEffortPath(heights)

    print("\noutput:", serialize(ans))

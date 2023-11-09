# Created by Jones at 2023/11/09 13:35
# leetgo: dev
# https://leetcode.cn/problems/escape-the-spreading-fire/

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
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:  # fire
                    q.append((i, j))

        time = [[inf] * n for _ in range(m)]
        for x, y in q:
            time[x][y] = 0

        dirs = [0, -1, 0, 1, 0]
        while q:
            qn = len(q)
            for _ in range(qn):
                x, y = q.popleft()
                for dx, dy in pairwise(dirs):
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and grid[nx][ny] != 2
                        and time[nx][ny] == inf
                    ):
                        time[nx][ny] = time[x][y] + 1
                        q.append((nx, ny))

        q = deque([(0, 0)])

        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0

        while q:
            x, y = q.popleft()
            for dx, dy in pairwise(dirs):
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and grid[nx][ny] != 2
                    and dist[nx][ny] == inf
                ):
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        if dist[-1][-1] == inf:
            return -1
        if time[-1][-1] == inf:
            return 10**9
        res = time[-1][-1] - dist[-1][-1]
        if res < 0:
            return -1
        if dist[-1][-2] + res < time[-1][-2] or dist[-2][-1] + res < time[-2][-1]:
            return res
        return res - 1


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumMinutes(grid)

    print("\noutput:", serialize(ans))

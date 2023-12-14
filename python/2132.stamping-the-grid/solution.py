# Created by Jones at 2023/12/14 17:59
# leetgo: dev
# https://leetcode.cn/problems/stamping-the-grid/

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
    def possibleToStamp(self, grid: List[List[int]], height: int, width: int) -> bool:
        if height == width == 1:
            return True
        m = len(grid)
        n = len(grid[0])

        # prefix sum
        p = [[0] * (n + 1) for _ in range(m + 1)]

        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                p[i][j] = x + p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1]

        # diff array
        d = [[0] * (n + 2) for _ in range(m + 2)]
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                r, c = i + height - 1, j + width - 1
                if r > m or c > n:
                    continue

                cur_sum = p[r][c] - p[r][j-1] - p[i-1][c] + p[i-1][j-1]
                if cur_sum == 0:
                    d[i][j] += 1
                    d[r + 1][j] -= 1
                    d[i][c + 1] -= 1
                    d[r + 1][c + 1] += 1


        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                d[i][j] += d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1]
                if x == 0 and d[i][j] == 0:
                    return False
        return True


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    stampHeight: int = deserialize("int", read_line())
    stampWidth: int = deserialize("int", read_line())
    ans = Solution().possibleToStamp(grid, stampHeight, stampWidth)

    print("\noutput:", serialize(ans))

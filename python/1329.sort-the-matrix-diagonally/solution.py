# Created by Jones at 2024/04/29 12:36
# leetgo: 1.4.5
# https://leetcode.cn/problems/sort-the-matrix-diagonally/

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
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # left
        for i in range(m):
            x, y = i, 0
            q = []
            while x < m and y < n:
                q.append(mat[x][y])
                x += 1
                y += 1
            x, y = i, 0
            q.sort(reverse=True)
            while x < m and y < n:
                mat[x][y] = q.pop()
                x += 1
                y += 1

        # top
        for j in range(1, n):
            x, y = 0, j
            q = []
            while x < m and y < n:
                q.append(mat[x][y])
                x += 1
                y += 1
            x, y = 0, j
            q.sort(reverse=True)
            while x < m and y < n:
                mat[x][y] = q.pop()
                x += 1
                y += 1

        return mat


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().diagonalSort(mat)
    print("\noutput:", serialize(ans, "integer[][]"))

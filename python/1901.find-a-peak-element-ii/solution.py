# Created by Jones at 2023/12/19 14:25
# leetgo: dev
# https://leetcode.cn/problems/find-a-peak-element-ii/

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
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        # search the good row
        left = 0
        right = m - 1
        while left < right:
            mid = (left + right) >> 1
            if max(mat[mid]) > max(mat[mid + 1]):
                right = mid
            else:
                left = mid + 1
        row = mat[right]
        mx = max(row)

        return [right, row.index(mx)]

        # search the peek of good row
        # l = 0
        # r = n - 1
        # while l < r:
        #     mid = (l + r) >> 1
        #     if row[mid] > row[mid + 1]:
        #         r = mid
        #     else:
        #         l = mid + 1

        # print(i, r)

        # if (i == 0 or mat[i][r] > mat[i - 1][r]) and (
        #     i == m - 1 or mat[i][r] > mat[i + 1][r]
        # ):
        #     return [i, r]
        # return [-1, -1]


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findPeakGrid(mat)

    print("\noutput:", serialize(ans))

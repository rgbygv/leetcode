# Created by Jones at 2023/12/01 21:39
# leetgo: dev
# https://leetcode.cn/problems/first-completely-painted-row-or-column/

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
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row = [0] * m
        col = [0] * n

        mp = {x: (i, j) for i, row in enumerate(mat) for j, x in enumerate(row)}

        for idx, x in enumerate(arr):
            i, j = mp[x]
            row[i] += 1
            col[j] += 1
            if row[i] == n or col[j] == m:
                return idx

        return -1


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().firstCompleteIndex(arr, mat)

    print("\noutput:", serialize(ans))

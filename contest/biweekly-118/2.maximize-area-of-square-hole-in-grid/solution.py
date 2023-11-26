# Created by Jones at 2023/11/25 22:30
# leetgo: dev
# https://leetcode.cn/problems/maximize-area-of-square-hole-in-grid/
# https://leetcode.cn/contest/biweekly-contest-118/problems/maximize-area-of-square-hole-in-grid/

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
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def f(v):
            n = len(v)
            i = 0
            res = 1
            while i < n:
                j = i + 1
                while j < n and v[j] - v[j - 1] == 1:
                    j += 1
                res = max(res, j - i)
                i = j
            return res + 1

        return min(f(sorted(hBars)), f(sorted(vBars))) ** 2

        # h = [1] + sorted(hBars) + [n + 2]
        # v = [1] + sorted(vBars) + [m + 2]

        # # print(h, v)
        # res = 0
        # s = set()
        # for r, x in enumerate(h):
        #     for l in range(r):
        #         size = x - h[l]
        #         s.add(size)

        # # print(s)
        # for r, x in enumerate(v):
        #     for l in range(r):
        #         size = x - v[l]
        #         if size in s:
        #             res = max(res, size**2)
        # return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    hBars: List[int] = deserialize("List[int]", read_line())
    vBars: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximizeSquareHoleArea(n, m, hBars, vBars)

    print("\noutput:", serialize(ans))

# Created by Jones at 2023/11/19 10:30
# leetgo: dev
# https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/
# https://leetcode.cn/contest/weekly-contest-372/problems/find-building-where-alice-and-bob-can-meet/

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
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(heights)
        right = [n] * (n)
        st = []
        for i, h in enumerate(heights):
            while st and h > heights[st[-1]]:
                right[st.pop()] = i
            st.append(i)

        res = []

        @cache
        def f(y, hx):
            if y == n:
                return -1
            if heights[y] > hx:
                return y
            return f(right[y], hx)

        for x, y in queries:
            if x > y:
                x, y = y, x
            if heights[y] > heights[x] or x == y:
                res.append(y)
                continue
            res.append(f(y, heights[x]))

        return res


# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().leftmostBuildingQueries(heights, queries)

    print("\noutput:", serialize(ans))

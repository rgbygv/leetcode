# Created by Jones at 2023/10/27 21:20
# leetgo: dev
# https://leetcode.cn/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

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
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        mod = 10**9 + 7
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()

        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()

        max_h = max(y - x for x, y in pairwise(sorted(horizontalCuts)))
        max_w = max(y - x for x, y in pairwise(sorted(verticalCuts)))

        return max_h * max_w % mod


# @lc code=end

if __name__ == "__main__":
    h: int = deserialize("int", read_line())
    w: int = deserialize("int", read_line())
    horizontalCuts: List[int] = deserialize("List[int]", read_line())
    verticalCuts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(h, w, horizontalCuts, verticalCuts)

    print("\noutput:", serialize(ans))

# Created by Jones at 2023/11/08 14:07
# leetgo: dev
# https://leetcode.cn/problems/determine-if-a-cell-is-reachable-at-a-given-time/

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
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        x = abs(sx - fx)
        y = abs(sy - fy)
        return max(x, y) <= t


# @lc code=end

if __name__ == "__main__":
    sx: int = deserialize("int", read_line())
    sy: int = deserialize("int", read_line())
    fx: int = deserialize("int", read_line())
    fy: int = deserialize("int", read_line())
    t: int = deserialize("int", read_line())
    ans = Solution().isReachableAtTime(sx, sy, fx, fy, t)

    print("\noutput:", serialize(ans))

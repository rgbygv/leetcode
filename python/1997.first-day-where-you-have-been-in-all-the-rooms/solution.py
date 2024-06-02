# Created by Jones at 2024/06/02 12:18
# leetgo: 1.4.7
# https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nextVisit)

        f = [0] * (n + 1)
        p = [0] * (n + 1)
        for i, x in enumerate(nextVisit):
            f[i] = f[i - 1] + 2
            if x != i:
                f[i] += p[i] - p[x]  # sum(f[x:i])
            f[i] %= mod
            p[i + 1] = f[i]
        # ic(f)
        return f[n - 2]


# @lc code=end

if __name__ == "__main__":
    nextVisit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().firstDayBeenInAllRooms(nextVisit)
    print("\noutput:", serialize(ans, "integer"))

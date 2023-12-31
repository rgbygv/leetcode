# Created by Bob at 2023/12/31 14:03
# leetgo: dev
# https://leetcode.cn/problems/day-of-the-year/

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


class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def ok(year: int):
            return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

        year, month, day = map(int, date.split("-"))
        T = 0
        if ok(year):
            days[1] += 1
        T += sum(days[: month - 1])
        T += day
        return T


# @lc code=end

if __name__ == "__main__":
    date: str = deserialize("str", read_line())
    ans = Solution().dayOfYear(date)

    print("\noutput:", serialize(ans))

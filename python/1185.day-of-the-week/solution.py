# Created by Bob at 2023/12/30 19:50
# leetgo: dev
# https://leetcode.cn/problems/day-of-the-week/

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
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # - 给出的日期一定是在 `1971` 到 `2100` 年之间的有效日期。
        p = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def ok(year: int):
            return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

        T = 5  # 1971-01-01 Friday
        if ok(year):
            days[1] += 1
        T += sum(days[: month - 1])
        T += day
        for y in range(1971, year):
            T += 365 + ok(y)

        return p[(T - 1) % 7]


# @lc code=end

if __name__ == "__main__":
    day: int = deserialize("int", read_line())
    month: int = deserialize("int", read_line())
    year: int = deserialize("int", read_line())
    ans = Solution().dayOfTheWeek(day, month, year)

    print("\noutput:", serialize(ans))

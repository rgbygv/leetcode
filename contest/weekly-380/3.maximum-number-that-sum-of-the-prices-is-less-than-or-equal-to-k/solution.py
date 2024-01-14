# Created by Jones at 2024/01/14 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
# https://leetcode.cn/contest/weekly-contest-380/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

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

N = 50


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        l = 1
        r = 1 << 50

        @cache
        def f(mid: int):
            if mid == 0:
                return 0
            n = mid.bit_length()
            rest = mid ^ (1 << (n - 1))
            # print(mid, rest)
            if n % x == 0:
                return rest + 1 + f(rest) + f((1 << (n - 1)) - 1)
            return f(rest) + f((1 << (n - 1)) - 1)

        while l < r:
            mid = (l + r + 1) >> 1
            cnt = f(mid)
            # print(mid, cnt)
            if cnt > k:
                r = mid - 1
            else:
                l = mid
        return l


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().findMaximumNumber(k, x)

    print("\noutput:", serialize(ans))

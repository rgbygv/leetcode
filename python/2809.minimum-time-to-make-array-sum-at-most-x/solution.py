# Created by Jones at 2024/01/19 13:35
# leetgo: dev
# https://leetcode.cn/problems/minimum-time-to-make-array-sum-at-most-x/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional


# @lc code=begin


class Solution:
    def minimumTime(self, a: List[int], b: List[int], x: int) -> int:
        n = len(a)
        q = sorted(zip(b, a))

        f = [[0] * (n + 1) for _ in range(n + 1)]

        sa = sum(a)
        sb = sum(b)
        for i, (b, a) in enumerate(q, 1):
            for t in range(1, i + 1):
                f[i][t] = max(f[i - 1][t], f[i - 1][t - 1] + a + b * t)
        # pprint(f)
        for t in range(0, n + 1):
            if sa + sb * t - f[n][t] <= x:
                return t
        return -1


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minimumTime(nums1, nums2, x)

    print("\noutput:", serialize(ans))

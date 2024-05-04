# Created by Jones at 2024/05/04 14:56
# leetgo: 1.4.6
# https://leetcode.cn/problems/maximum-of-absolute-value-expression/

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
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # - `2 <= arr1.length == arr2.length <= 40000`
        # - `-10^6 <= arr1[i], arr2[i] <= 10^6`

        # `|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|`

        def handle(a: list[int]):
            # assume i > j
            # a[i] - a[j] + i- j || a[j] - a[i] + i - j
            # a[i] + i - (a[j] + j) || a[j] - j - (a[i] - i)

            # record min a[j]+j, and max a[j] - j
            mn = inf
            mx = -inf
            res = 0

            for i, x in enumerate(a):
                res = max(res, x + i - mn, mx - (x - i))
                mn = min(mn, x + i)
                mx = max(mx, x - i)
            return res

        return max(
            handle(x + y for x, y in zip(arr1, arr2)),
            handle(x - y for x, y in zip(arr1, arr2)),
        )


# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxAbsValExpr(arr1, arr2)
    print("\noutput:", serialize(ans, "integer"))

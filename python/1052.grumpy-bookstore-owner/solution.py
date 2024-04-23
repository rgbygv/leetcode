# Created by Jones at 2024/04/23 11:39
# leetgo: 1.4.5
# https://leetcode.cn/problems/grumpy-bookstore-owner/

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
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # - `n == customers.length == grumpy.length`
        # - `1 <= minutes <= n <= 2 * 10⁴`
        # - `0 <= customers[i] <= 1000`
        # - `grumpy[i]` is either `0` or `1`.

        n = len(customers)
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] += suf[i + 1] + customers[i] * (1 - grumpy[i])

        p = list(accumulate(customers, initial=0))

        s = 0
        res = 0
        for i in range(n):
            # use skill time[i]
            end = min(i + minutes, n)
            res = max(res, s + p[end] - p[i] + suf[end])
            s += customers[i] * (1 - grumpy[i])
        return res


# @lc code=end

if __name__ == "__main__":
    customers: List[int] = deserialize("List[int]", read_line())
    grumpy: List[int] = deserialize("List[int]", read_line())
    minutes: int = deserialize("int", read_line())
    ans = Solution().maxSatisfied(customers, grumpy, minutes)
    print("\noutput:", serialize(ans, "integer"))

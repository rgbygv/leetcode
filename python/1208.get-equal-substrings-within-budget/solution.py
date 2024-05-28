# Created by Jones at 2024/05/28 10:46
# leetgo: 1.4.7
# https://leetcode.com/problems/get-equal-substrings-within-budget/

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
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        q = list(abs(ord(x) - ord(y)) for x, y in zip(s, t))
        q.append(inf)  # handle situaition sum(q[i:]) == maxCost
        n = len(q)
        l = r = 0
        cost = 0
        res = 0
        while r < n:
            while r < n and cost <= maxCost:
                cost += q[r]
                r += 1
            res = max(res, r - l - 1)
            cost -= q[l]
            l += 1

        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    maxCost: int = deserialize("int", read_line())
    ans = Solution().equalSubstring(s, t, maxCost)
    print("\noutput:", serialize(ans, "integer"))

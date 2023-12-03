# Created by Jones at 2023/12/03 10:30
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-infection-sequences/
# https://leetcode.cn/contest/weekly-contest-374/problems/count-the-number-of-infection-sequences/

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
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        mod = 10**9 + 7
        left = sick[0] - 0
        right = n - 1 - sick[-1]
        p = []

        for a in (left, right):
            if a != 0:
                p.append((a, False))

        for x, y in pairwise(sick):
            a = y - x - 1
            if a != 0:
                p.append((a, True))
            # res = res * (pow(2, a - 1, mod)) % mod
        res = 1
        p.sort()

        if p:
            res = p.pop()[0] + 1
        ok = False
        for x, t in p:
            if t:
                ok = True
                res = res * (pow(2, x - 1, mod)) % mod
            else:
                res = res * x % mod
        if len(p) == 0 and not ok:
            return 1
        return (res) % mod


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    sick: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfSequence(n, sick)

    print("\noutput:", serialize(ans))

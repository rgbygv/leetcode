# Created by Jones at 2023/12/08 13:51
# leetgo: dev
# https://leetcode.cn/problems/maximum-earnings-from-taxi/

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
class BIT:
    def __init__(self, n: int) -> None:
        self.q = [0] * (n + 1)

    def lowbit(self, x: int):
        return x & -x

    def update(self, i: int, x: int):
        while i < len(self.q):
            self.q[i] = max(self.q[i], x)
            i += self.lowbit(i)

    def query(self, x: int) -> int:
        res = 0
        while x > 0:
            res = max(res, self.q[x])
            x -= self.lowbit(x)
        return res


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        f = [0] * (n + 1)
        rides.sort(key=lambda e: e[1])
        bit = BIT(n)

        for x, y, tip in rides:
            f[y] = max(f[y], bit.query(x) + y - x + tip)
            bit.update(y, f[y])

        return max(f)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rides: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTaxiEarnings(n, rides)

    print("\noutput:", serialize(ans))

# Created by Jones at 2024/05/03 14:08
# leetgo: 1.4.5
# https://leetcode.cn/problems/last-stone-weight-ii/

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
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # - `1 <= stones.length <= 30`
        # - `1 <= stones[i] <= 100`
        stones.sort()
        n = len(stones)
        # ic(stones, sum(stones))
        s = sum(stones)
        m = s // 2 + 1
        f = [False] * (m)
        f[0] = True

        for x in stones:
            # j + x < m
            for j in range(m - x - 1, -1, -1):
                if f[j]:
                    f[j + x] = True

        res = inf
        for x, ok in enumerate(f):
            if ok:
                res = min(res, abs(s - 2 * x))
        return res

        # we can combine any two stones
        # if we have 3 s, a b c
        # if n == 1:
        #     return stones[0]
        # if n == 2:
        #     return stones[-1] - stones[0]
        # res = 100
        # # ic(stones)
        # for i in range(1, n):
        #     stones[i] -= stones[0]
        #     res = min(res, self.lastStoneWeightII(stones[1:]))
        #     stones[i] += stones[0]
        # return res


# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lastStoneWeightII(stones)
    print("\noutput:", serialize(ans, "integer"))

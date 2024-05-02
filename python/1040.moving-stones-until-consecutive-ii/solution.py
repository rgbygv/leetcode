# Created by Jones at 2024/05/02 20:17
# leetgo: 1.4.5
# https://leetcode.cn/problems/moving-stones-until-consecutive-ii/

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
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        # compute max
        mx = max(stones[n - 2] - stones[0], stones[n - 1] - stones[1]) - n + 2
        # compute min
        q = []
        for x, y in pairwise(stones):
            d = y - x - 1
            if d > 0:
                q.append(d)
        if len(q) == 1:
            mn = min(2, mx)
        else:
            stay = 0
            n = len(stones)
            l = 0
            r = 0
            while r < n:
                while r < n and stones[r] <= stones[l] + n - 1:
                    # ic(stones[l : r + 1])
                    r += 1
                stay = max(stay, r - l)
                l += 1
            mn = n - stay
        return [mn, mx]


# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numMovesStonesII(stones)
    print("\noutput:", serialize(ans, "integer[]"))

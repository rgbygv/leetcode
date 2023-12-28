# Created by Bob at 2023/12/28 13:26
# leetgo: dev
# https://leetcode.cn/problems/collecting-chocolates/

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
    def minCost(self, nums: List[int], x: int) -> int:
        # assume we use << t times
        # the cost is the min(nums[i:i+t+1]) + t * x
        n = len(nums)
        res = inf
        nums = nums + nums
        for t in range(n):
            cost = 0
            q = []
            to_del = []
            for r in range(t):
                heappush(q, nums[r])
            for l, r in zip(range(n), range(t, t + n)):
                heappush(q, nums[r])
                while to_del and q[0] == to_del[0]:
                    heappop(to_del)
                    heappop(q)
                cost += q[0]
                heappush(to_del, nums[l])
            res = min(res, cost + t * x)

        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minCost(nums, x)

    print("\noutput:", serialize(ans))

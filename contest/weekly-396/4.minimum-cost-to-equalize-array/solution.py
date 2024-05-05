# Created by Jones at 2024/05/05 20:55
# leetgo: 1.4.6
# https://leetcode.cn/problems/minimum-cost-to-equalize-array/
# https://leetcode.cn/contest/weekly-contest-396/problems/minimum-cost-to-equalize-array/

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
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return (nums[-1] - nums[0]) * cost1 % mod
        mx = nums[-1]
        s = sum(nums)
        if 2 * cost1 <= cost2:
            return cost1 * (mx * n - s) % mod
        # we should use cost2 first

        # don't know how to deal with that x maybe larger than max
        # but i know the x will not larger than max too much

        def f(a, s):
            if s & 1 == 0:
                if a[-1] * 2 <= s:  # we can use all cost2
                    return s // 2 * cost2
                else:
                    # a[-1] is too much, assume we use all cost1 for a[-1] -rest
                    # rather we need increase max, and we target is to make
                    # (a[-1] + x) * 2 <= s + n * x
                    #  x >= (2*a[-1] - s) // (n-2)
                    rest = s - a[-1]
                    return rest * cost2 + (a[-1] - rest) * cost1
            else:
                if a[-1] * 2 <= s + 1:  # we can use all cost2 and only 1 cost1
                    return s // 2 * cost2 + cost1
                else:
                    # a[-1] is too much, assume we use all cost1
                    rest = s - a[-1]
                    return rest * cost2 + (a[-1] - rest) * cost1

        a = [mx - x for x in nums[::-1]]
        s = sum(a)
        res = f(a, s)
        for _ in range(a[-1] + 1):
            s += n
            a[-1] += 1
            res = min(res, f(a, s))
        return res % mod


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    cost1: int = deserialize("int", read_line())
    cost2: int = deserialize("int", read_line())
    ans = Solution().minCostToEqualizeArray(nums, cost1, cost2)
    print("\noutput:", serialize(ans, "integer"))

# Created by Jones at 2024/05/11 15:01
# leetgo: 1.4.7
# https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/

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
    def waysToSplit(self, nums: List[int]) -> int:
        """
        - `3 <= nums.length <= 10⁵`
        - `0 <= nums[i] <= 10⁴`
        """
        mod = 10**9 + 7
        n = len(nums)
        p = list(accumulate(nums, initial=0))

        res = 0
        # sum([..l]) < sum[l..mid] < sum[mid..]
        for l in range(1, n - 1):
            if p[l] * 3 > p[-1]:
                break
            # we use binary search, and can use two pointer simulate
            # p[mid] - p[l] >= [l]
            mid_start = bisect_left(p, p[l] * 2, lo=l + 1)
            # p[-1] - p[mid] >= p[mid] - p[l] => p[mid] *2 <= p[-1] + p[l]
            # p[mid] * 2 < p[-1] + p[l] + 1
            mid_end = bisect_right(p, (p[-1] + p[l]) // 2, hi=n)
            # ic(l, mid_start, mid_end)
            if mid_end > mid_start:
                res += mid_end - mid_start

        return res % mod


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().waysToSplit(nums)
    print("\noutput:", serialize(ans, "integer"))

# Created by Jones at 2023/11/20 14:26
# leetgo: dev
# https://leetcode.cn/problems/maximum-subarray/

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
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        if res <= 0:
            return res
        s = p = 0
        for x in nums:
            s += x
            res = max(res, s - p)
            p = min(p, s)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)

    print("\noutput:", serialize(ans))

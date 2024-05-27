# Created by Jones at 2024/05/27 08:21
# leetgo: 1.4.7
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

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
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 1
        r = n
        while l <= r:
            mid = (l + r) >> 1
            cnt = n - bisect_left(nums, mid)
            if cnt == mid:
                return mid
            if cnt < mid:
                r = mid - 1
            else:
                l = mid + 1
        return -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().specialArray(nums)
    print("\noutput:", serialize(ans, "integer"))

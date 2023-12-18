# Created by Jones at 2023/12/18 16:01
# leetgo: dev
# https://leetcode.cn/problems/find-peak-element/

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
    def findPeakElement(self, a: List[int]) -> int:
        n = len(a)
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) >> 1
            if a[mid + 1] < a[mid]:
                r = mid
            else:
                l = mid + 1
        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findPeakElement(nums)

    print("\noutput:", serialize(ans))

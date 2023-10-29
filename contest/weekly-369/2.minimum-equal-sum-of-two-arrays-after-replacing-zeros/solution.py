# Created by Jones at 2023/10/29 10:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
# https://leetcode.cn/contest/weekly-contest-369/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

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
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = nums1.count(0)
        s1 = sum(nums1)

        b = nums2.count(0)
        s2 = sum(nums2)

        if a == 0 and b == 0 and s1 != s2:
            return -1

        if a == 0 and s2 + b > s1:
            return -1

        if b == 0 and s1 + a > s2:
            return -1

        if a == 0 and b == 0:
            return s1

        if s1 == s2:
            return s1 + max(a, b)

        return max(s1 + a, s2 + b)


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSum(nums1, nums2)

    print("\noutput:", serialize(ans))

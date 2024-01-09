# Created by Jones at 2024/01/09 20:52
# leetgo: dev
# https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/
# https://leetcode.cn/contest/weekly-contest-379/problems/maximum-size-of-a-set-after-removals/

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
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        s1 = set(nums1)
        s2 = set(nums2)

        same = s1 & s2

        s1 -= same
        s2 -= same

        half = n >> 1
        res = 0
        a, b, c = len(s1), len(s2), len(same)
        if a >= half:
            res += half
        else:
            k = min(c, half - a)
            res += a + k
            c -= k

        if b >= half:
            res += half
        else:
            k = min(c, half - b)
            res += b + k
            c -= k

        return res


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSetSize(nums1, nums2)

    print("\noutput:", serialize(ans))

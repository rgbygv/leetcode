# Created by Jones at 2023/11/12 10:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-operations-to-maximize-last-elements-in-arrays/
# https://leetcode.cn/contest/weekly-contest-371/problems/minimum-operations-to-maximize-last-elements-in-arrays/

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
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a, b = nums1[-1], nums2[-1]
        res = 0
        # don't change last
        for i in range(n):
            x, y = nums1[i], nums2[i]
            if x <= a and y <= b:
                continue
            if y <= a and x <= b:
                res += 1
            else:
                res = inf
                break
        res2 = 1
        a, b = b, a
        for i in range(n - 1):
            x, y = nums1[i], nums2[i]
            if x <= a and y <= b:
                continue
            if y <= a and x <= b:
                res2 += 1
            else:
                res2 = inf
                break

        res = min(res, res2)
        if res == inf:
            return -1
        return res


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums1, nums2)

    print("\noutput:", serialize(ans))

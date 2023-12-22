# Created by Jones at 2023/12/22 19:29
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/

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
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def LIS():
            pre = [0] * n
            q = []
            for i, x in enumerate(nums):
                j = bisect_left(q, x)
                pre[i] = j + 1
                if j >= len(q):
                    q.append(x)
                else:
                    q[j] = x
            return pre

        pre = LIS()
        q = []
        res = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            j = bisect_left(q, x)
            suf = j + 1
            if suf >= 2 and pre[i] >= 2:
                res = max(res, suf + pre[i] - 1)
            if j >= len(q):
                q.append(x)
            else:
                q[j] = x
        return n - res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumMountainRemovals(nums)

    print("\noutput:", serialize(ans))

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
        def LIS(l: int, r: int):
            # longest increase sub array
            q = []
            for i in range(l, r + 1) if l < r else range(l, r - 1, -1):
                x = nums[i]
                if not q or x > q[-1]:
                    q.append(x)
                else:
                    j = bisect_left(q, x)
                    q[j] = x
            return q

        res = 0
        n = len(nums)
        for i in range(1, n - 1):
            # if i as top
            # find the longest up array
            left = LIS(0, i)
            right = LIS(n - 1, i)
            if min(len(left), len(right)) <= 1:
                continue
            # print(i, left, right)
            if left[-1] == right[-1]:
                res = max(res, len(left) + len(right) - 1)
            else:
                res = max(res, len(left) + len(right))
        return n - res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumMountainRemovals(nums)

    print("\noutput:", serialize(ans))

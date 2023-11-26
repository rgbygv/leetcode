# Created by Jones at 2023/11/25 22:30
# leetgo: dev
# https://leetcode.cn/problems/find-maximum-non-decreasing-array-length/
# https://leetcode.cn/contest/biweekly-contest-118/problems/find-maximum-non-decreasing-array-length/

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
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        p = list(accumulate(nums, initial=0))
        # greedy
        # i = 0
        # res = 0
        # last = 0
        # while i < n:
        #     if nums[i] >= last:
        #         res += 1
        #         last = nums[i]
        #         i += 1
        #     else:
        #         if p[-1] - p[i] < last:
        #             break
        #         j = bisect_left(p, last + p[i])
        #         print(i, j, last, p[j] - p[i])
        #         left = p[i]
        #         while p[j] - p[i] >= last + p[i] - left:
        #             i += 1
        #         print(i, j, last, p[j] - p[i])
        #         last = p[j] - p[i - 1]
        #         res += 1
        #         i = j
        # return res

        # @cache
        # def dfs(i: int, last: int):
        #     if i == n:
        #         return 0
        #     if nums[i] >= last:
        #         return 1 + dfs(i + 1, nums[i])
        #     # a[i..j] >= last
        #     # p[j] - p[i] >= last
        #     if p[-1] - p[i] < last:
        #         return 0
        #     j = bisect_left(p, last + p[i])
        #     # print(i, last, j, p[j] - p[i])
        #     return max(
        #         dfs(i + 1, last + nums[i]),
        #         1 + dfs(j, p[j] - p[i]),
        #     )

        # res = dfs(0, 0)
        # dfs.cache_clear()
        # if res == -inf:
        #     return 1
        # return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMaximumLength(nums)

    print("\noutput:", serialize(ans))

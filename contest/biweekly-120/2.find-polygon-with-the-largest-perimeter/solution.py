# Created by Jones at 2023/12/23 22:30
# leetgo: dev
# https://leetcode.cn/problems/find-polygon-with-the-largest-perimeter/
# https://leetcode.cn/contest/biweekly-contest-120/problems/find-polygon-with-the-largest-perimeter/

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
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        p = list(accumulate(nums, initial=0))
        res = -1
        for i in range(2, len(p)-1):
            # print(nums, nums[i], p[i])
            if nums[i] < p[i]:
                res = max(res, nums[i] + p[i])
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestPerimeter(nums)

    print("\noutput:", serialize(ans))

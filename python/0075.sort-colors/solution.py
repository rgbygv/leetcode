# Created by Jones at 2024/06/12 13:26
# leetgo: 1.4.7
# https://leetcode.com/problems/sort-colors/

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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for x in nums:
            cnt[x] += 1

        start = 0
        for x, size in enumerate(cnt):
            for i in range(start, start + size):
                nums[i] = x
            start += size

        # n = len(nums)
        # i = l = 0
        # j = r = n - 1
        # """
        # move 0 left, move 2 right
        # Input: nums = [2,0,2,1,1,0]
        # """
        # while l < r:
        #     while l < r and nums[l] == 0:
        #         l += 1
        #         i += 1
        #     while l < r and nums[r] == 2:
        #         r -= 1
        #         j -= 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().sortColors(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))

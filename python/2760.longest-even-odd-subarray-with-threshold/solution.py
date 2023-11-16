# Created by Jones at 2023/11/16 12:44
# leetgo: dev
# https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/

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
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            if nums[i] & 1 or nums[i] > threshold:
                i += 1
                continue
            j = i + 1
            while j < n and nums[j] & 1 != nums[j - 1] & 1 and nums[j] <= threshold:
                j += 1
            res = max(res, j - i)
            i = j
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().longestAlternatingSubarray(nums, threshold)

    print("\noutput:", serialize(ans))

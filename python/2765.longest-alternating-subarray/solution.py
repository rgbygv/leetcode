# Created by Jones at 2024/01/23 16:07
# leetgo: dev
# https://leetcode.cn/problems/longest-alternating-subarray/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = -1
        while i < n:
            j = i + 1
            while j < n and nums[j] - nums[j - 1] == (1 if (j - i) & 1 else -1):
                j += 1
            res = max(res, j - i)
            i = j
            if i < n and nums[i] - nums[i - 1] == 1:
                i = j - 1
        return -1 if res < 2 else res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().alternatingSubarray(nums)

    print("\noutput:", serialize(ans))

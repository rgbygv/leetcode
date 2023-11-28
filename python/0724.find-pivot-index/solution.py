# Created by Jones at 2023/11/28 16:39
# leetgo: dev
# https://leetcode.cn/problems/find-pivot-index/

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
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left = 0
        for i,x in enumerate(nums):
            s -= x
            if s == left:
                return i
            left += x
        return -1

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().pivotIndex(nums)

    print("\noutput:", serialize(ans))

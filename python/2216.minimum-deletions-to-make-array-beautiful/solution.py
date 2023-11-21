# Created by Jones at 2023/11/21 15:48
# leetgo: dev
# https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/

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
    def minDeletion(self, nums: List[int]) -> int:
        res = 0
        i = 0
        n = len(nums)
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[j - 1]:
                j += 1
            # a[i] also need to be deleted
            if j == n:
                j += 1
            res += j - i - 1
            i = j + 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minDeletion(nums)

    print("\noutput:", serialize(ans))

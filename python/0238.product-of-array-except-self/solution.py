# Created by Jones at 2023/11/28 16:42
# leetgo: dev
# https://leetcode.cn/problems/product-of-array-except-self/

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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in reversed(range(n - 1)):
            suf[i] = nums[i] * suf[i + 1]
        # for res[n-1]
        suf.append(1)

        res = [0] * n
        left = 1
        for i, x in enumerate(nums):
            res[i] = left * suf[i + 1]
            left *= x
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)

    print("\noutput:", serialize(ans))

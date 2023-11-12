# Created by Jones at 2023/11/12 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-strong-pair-xor-ii/
# https://leetcode.cn/contest/weekly-contest-371/problems/maximum-strong-pair-xor-ii/

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # `|x - y| <= min(x, y)`

        # assume x < y
        # y - x <= x

        # x < y <= 2x
        nums = sorted(set(nums))
        res = 0
        l = 0
        for r, y in enumerate(nums):
            while nums[l] * 2 < y:
                l += 1
            # find [l..r] ^ y
            # y = 101110
            L = l
            R = r - 1
            tmp = 0
            for i in range(y.bit_length() - 1, -1, -1):
                if y >> i & 1:
                    j = bisect_left(nums, 1 << i, lo=L, hi=R) - 1
                    if j >= L:
                        R = j
                        tmp |= 1 << i
                else:
                    j = bisect_left(nums, 1 << i, lo=L, hi=R)
                    if j <= R:
                        L = j
                        tmp |= 1 << i
                if L > R:
                    break
            res = max(res, tmp)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumStrongPairXor(nums)

    print("\noutput:", serialize(ans))

# Created by Jones at 2023/11/04 14:12
# leetgo: dev
# https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/

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
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        N = max(nums).bit_length()
        mask = 0
        for i in range(N, -1, -1):
            mask |= 1 << i
            new = res | (1 << i)
            seen = set()
            for x in nums:
                x &= mask
                if new ^ x in seen:
                    res = new
                    break
                seen.add(x)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMaximumXOR(nums)

    print("\noutput:", serialize(ans))

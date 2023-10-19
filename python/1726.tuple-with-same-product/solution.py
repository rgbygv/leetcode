# Created by Jones at 2023/10/19 14:02
# leetgo: dev
# https://leetcode.cn/problems/tuple-with-same-product/

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
    def tupleSameProduct(self, nums: List[int]) -> int:
        mp = Counter()
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i):
                cur = nums[i] * nums[j]
                res += mp[cur]
                mp[cur] += 1
        return res * 8


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().tupleSameProduct(nums)

    print("\noutput:", serialize(ans))

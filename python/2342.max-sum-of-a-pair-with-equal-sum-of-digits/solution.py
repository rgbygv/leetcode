# Created by Jones at 2023/11/18 15:02
# leetgo: dev
# https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

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
    def maximumSum(self, nums: List[int]) -> int:
        mp = defaultdict(list)
        for x in nums:
            s = 0
            y = x
            while x:
                s += x % 10
                x //= 10
            heappush(mp[s], y)
            if len(mp[s]) >= 3:
                heappop(mp[s])

        res = -1
        for v in mp.values():
            if len(v) == 2:
                res = max(res, sum(v))
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSum(nums)

    print("\noutput:", serialize(ans))

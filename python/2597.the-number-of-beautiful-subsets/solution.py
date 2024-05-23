# Created by Jones at 2024/05/23 16:37
# leetgo: 1.4.7
# https://leetcode.com/problems/the-number-of-beautiful-subsets/

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
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        - `1 <= nums.length <= 20`
        - `1 <= nums[i], k <= 1000`
        """
        nums.sort()
        n = len(nums)
        res = 0
        f = [[False] * n for _ in range(n)]
        for i, x in enumerate(nums):
            for j in range(i):
                if (x - nums[j]) == k:
                    f[i][j] = f[j][i] = True

        if all(x is False for v in f for x in v):
            return (1 << n) - 1

        @cache
        def dfs(i: int, ban: int):
            if i == n:
                return 1
            # can't choose a[i]
            if ban >> i & 1:
                return dfs(i + 1, ban)
            res = 0
            # don't choose a[i]
            res += dfs(i + 1, ban)
            # choose
            for d in range(n):
                if f[i][d]:
                    ban |= 1 << d
            res += dfs(i + 1, ban)
            return res

        return dfs(0, 0) - 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().beautifulSubsets(nums, k)
    print("\noutput:", serialize(ans, "integer"))

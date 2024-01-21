# Created by Jones at 2024/01/21 13:27
# leetgo: dev
# https://leetcode.cn/problems/split-array-largest-sum/

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
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = list(accumulate(nums, initial=0))

        def min(x: int, y: int):
            return x if x < y else y

        def max(x: int, y: int):
            return x if x > y else y

        # @cache
        # def dfs(i: int, k: int):
        #     if k == 1:
        #         return p[-1] - p[i]
        #     res = inf
        #     # n - j >= k-1 => j <= n - (k-1)
        #     for j in range(i + 1, n - (k - 1) + 1):
        #         res = min(res, max(p[j] - p[i], dfs(j, k - 1)))
        #     return res

        # res = dfs(0, k)

        f = [[0] * (k + 1) for _ in range(n)]

        for i in reversed(range(n)):
            f[i][1] = p[-1] - p[i]
            for kk in range(2, k + 1):
                for j in range(i + 1, n - (k - 1) + 1):
                    f[i][kk] = min(f[i][kk], max(p[j] - p[i], f[j][kk - 1]))

        return f[0][k]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().splitArray(nums, k)

    print("\noutput:", serialize(ans))

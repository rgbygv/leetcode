# Created by Jones at 2024/04/14 20:40
# leetgo: 1.4.5
# https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/
# https://leetcode.cn/contest/weekly-contest-393/problems/minimum-sum-of-values-by-dividing-array/

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
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)

        @cache
        def dfs(i: int, mask: int, j: int):
            if i == n:
                if j == m:
                    return 0
                return inf
            if j == m or (mask > 0 and mask < andValues[j]):
                return inf
            res = inf
            # split here
            cur = mask & nums[i]
            if cur == andValues[j]:
                res = nums[i] + dfs(i + 1, -1, j + 1)
            # don't split
            res = min(res, dfs(i + 1, cur, j))
            return res

        res = dfs(0, -1, 0)
        if res == inf:
            return -1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    andValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumValueSum(nums, andValues)
    print("\noutput:", serialize(ans, "integer"))

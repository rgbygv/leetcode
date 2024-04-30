# Created by Jones at 2024/04/30 15:37
# leetgo: 1.4.5
# https://leetcode.cn/problems/smallest-range-ii/

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
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[-1] - nums[0]
        # the minimal number should always +k
        # can we assume have `i`, a[..i] ⬆️ , a[i..] ⬇️
        for i in range(1, n):
            mn = min(nums[0] + k, nums[i] - k)
            mx = max(nums[i - 1] + k, nums[-1] - k)
            # print(i, mx, mn)
            res = min(res, mx - mn)
        return res

        # memory limit
        # @cache
        # def dfs(i: int, mx: int, mn: int):
        #     if i == n:
        #         nonlocal res
        #         res = min(res, mx - mn)
        #         return
        #     x = nums[i]
        #     # + k
        #     dfs(i + 1, max(mx, x + k), min(mn, x + k))
        #     # - k
        #     dfs(i + 1, max(mx, x - k), min(mn, x - k))

        # dfs(0, -inf, inf)
        # return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().smallestRangeII(nums, k)
    print("\noutput:", serialize(ans, "integer"))

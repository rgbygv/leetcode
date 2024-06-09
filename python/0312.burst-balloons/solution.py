# Created by Jones at 2024/06/09 14:09
# leetgo: 1.4.7
# https://leetcode.cn/problems/burst-balloons/

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
    def maxCoins(self, nums: List[int]) -> int:
        """
        - `n == nums.length`
        - `1 <= n <= 300`
        - `0 <= nums[i] <= 100`
        """
        nums = [1] + nums + [1]

        @cache
        def dfs(l: int, r: int) -> int:
            res = 0
            for mid in range(l + 1, r):
                res = max(
                    res,
                    nums[mid] * nums[l] * nums[r] + dfs(l, mid) + dfs(mid, r),
                )
            return res

        return dfs(0, len(nums) - 1)

        @cache
        def dfs(a: tuple[int]):
            n = len(a)
            if n == 1:
                return a[0]
            if n == 2:
                return a[0] * a[1] + max(a)
            # enumerate brust which balnoon
            res = 0
            for i in range(n):
                pre = a[i - 1] if i > 0 else 1
                suf = a[i + 1] if i < n - 1 else 1
                res = max(res, a[i] * pre * suf + dfs(a[:i] + a[i + 1 :]))
            return res

        return dfs(tuple(nums))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCoins(nums)
    print("\noutput:", serialize(ans, "integer"))

# Created by Jones at 2024/05/31 10:45
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-total-space-wasted-with-k-resizing-operations/

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
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """
        - `1 <= nums.length <= 200`
        - `1 <= nums[i] <= 10⁶`
        - `0 <= k <= nums.length - 1`

        Input: nums = [10,20,15,30,20], k = 2
        Output: 15
        Explanation: size = [10,20,20,30,30].
        """
        n = len(nums)
        if k + 1 == n:
            return 0
        k += 1
        # we split nums to `k+1` seg, and the ans is
        # sum(max(seg) * size(seg) - sum(seg) for each seg)

        p = list(accumulate(nums, initial=0))
        f = [[0] * n for _ in range(n)]
        for i, x in enumerate(nums):
            f[i][i] = x
            for j in range(i + 1, n):
                if nums[j] > x:
                    x = nums[j]
                f[i][j] = x

        def dfs(i: int, k: int):
            if k == 1:
                return f[0][i] * (i + 1) - p[i + 1]
            res = inf
            for j in range(i, -1, -1):
                res = min(
                    res, f[j][i] * (i - j + 1) - (p[i + 1] - p[j]) + dfs(j - 1, k - 1)
                )
            return res

        # return dfs(n-1,k)

        dp = [[inf] * (k + 1) for _ in range(n)]

        for i, x in enumerate(nums):
            for t in range(1, k + 1):
                if t == 1:
                    dp[i][t] = f[0][i] * (i + 1) - p[i + 1]
                    continue
                for j in range(i, 0, -1):
                    dp[i][t] = min(
                        dp[i][t],
                        f[j][i] * (i - j + 1) - (p[i + 1] - p[j]) + dp[j - 1][t - 1],
                    )
        # ic(dp)
        return dp[-1][-1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minSpaceWastedKResizing(nums, k)
    print("\noutput:", serialize(ans, "integer"))

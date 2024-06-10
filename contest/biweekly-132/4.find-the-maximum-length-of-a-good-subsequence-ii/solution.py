# Created by Jones at 2024/06/10 13:09
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-ii/
# https://leetcode.cn/contest/biweekly-contest-132/problems/find-the-maximum-length-of-a-good-subsequence-ii/

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
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        - `1 <= nums.length <= 5 * 10³`
        - `1 <= nums[i] <= 10⁹`
        - `0 <= k <= min(50, nums.length)`
        """
        n = len(nums)
        if k >= n - 1:
            return n
        if k == 0:
            return max(Counter(nums).values())

        last = [-1] * n
        mp = {}

        for i, x in enumerate(nums):
            if x in mp:
                last[i] = mp[x]
            mp[x] = i

        @cache
        def dfs(i: int, k: int):
            if i < 0:
                return 0
            res = 1 + dfs(last[i], k)
            if k > 0:
                """
                just quick query dfs(j,k-1)

                we can use BIT or Seg
                for j in range(0..i):
                    res = max(res, 1 + dfs(j, k-1) )
                """
                res = max(res, 1 + dfs(i - 1, k - 1))
            return res

        f = [0] * (n + 1)
        for _ in range(k):
            g = [0] * (n + 1)
            for i, x in enumerate(nums):
                g[i] = 1 + f[last[i]]

        return dfs(n - 1, k)

        @cache
        def dfs(i: int, k: int, j: int):
            if i < 0:
                return 0
            if k > i:
                return i + 1
            res = 0
            # choose
            if j == -1 or k - (nums[i] != nums[j]) >= 0:
                res = 1 + dfs(i - 1, k - (j != -1 and nums[i] != nums[j]), i)
            # don't
            res = max(res, dfs(i - 1, k, j))
            return res

        res = dfs(n - 1, k, -1)
        dfs.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumLength(nums, k)
    print("\noutput:", serialize(ans, "integer"))

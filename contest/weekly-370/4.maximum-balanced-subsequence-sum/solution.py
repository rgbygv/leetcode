# Created by Jones at 2023/11/05 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-balanced-subsequence-sum/
# https://leetcode.cn/contest/weekly-contest-370/problems/maximum-balanced-subsequence-sum/

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


class BIT:
    def __init__(self, n: int) -> None:
        self.n = n + 1
        self.q = {}

    def lowbit(self, x: int):
        return x & -x

    def update(self, x: int, val: int):
        while x < self.n:
            if x not in self.q or val > self.q[x]:
                self.q[x] = val
            x += self.lowbit(x)

    def query(self, x: int) -> int:
        res = -(10**18)
        while x > 0:
            if x in self.q and self.q[x] > res:
                res = self.q[x]
            x -= self.lowbit(x)
        return res


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        idx = [x - i for i, x in enumerate(nums)]
        n = len(nums)
        dp = [0] * n
        bit = BIT(n)
        print(idx)
        for i, x in enumerate(idx):
            if nums[i] <= 0:
                continue
            dp[x] = max(dp[x], bit.query(x) + nums[i])
            bit.update(x, dp[x])
            print(bit.q)

        return bit.query(max(idx))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxBalancedSubsequenceSum(nums)

    print("\noutput:", serialize(ans))

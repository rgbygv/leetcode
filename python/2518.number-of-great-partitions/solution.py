# Created by Jones at 2024/04/19 20:50
# leetgo: 1.4.5
# https://leetcode.cn/problems/number-of-great-partitions/

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
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        for i, x in enumerate(nums):
            # bigger then k is same as equal k
            if x > k:
                nums[i] = k

        s = sum(nums)
        # can't split to 2 group that >= k
        if s < 2 * k:
            return 0

        # k <= 1000
        # find >= k is hard, but < k is simple

        cnt = [0] * k
        cnt[0] = 1

        for x in nums:
            # i + x < k
            for i in range(k - x - 1, -1, -1):
                cnt[i + x] += cnt[i]
        # print(cnt)

        return (pow(2, n, mod) - sum(cnt) * 2) % mod

        # @cache
        # def dfs(i: int, s: int):
        #     if s < k:
        #         return
        #     cnt[s] += 1
        #     # choose nums[i]
        #     dfs(i + 1, s - nums[i])
        #     # don't choose nums[i]
        #     dfs(i + 1, s)

        # dfs(0, k)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countPartitions(nums, k)
    print("\noutput:", serialize(ans, "integer"))

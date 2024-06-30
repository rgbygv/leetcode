# Created by Jones at 2024/06/30 19:04
# leetgo: 1.4.7
# https://leetcode.cn/problems/target-sum/

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
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        - `1 <= nums.length <= 20`
        - `0 <= nums[i] <= 1000`
        - `0 <= sum(nums[i]) <= 1000`
        - `-1000 <= target <= 1000`
        """
        n = len(nums)

        @cache
        def dfs(i: int, target: int):
            if i == n:
                return target == 0
            return dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])

        return dfs(0, target)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findTargetSumWays(nums, target)
    print("\noutput:", serialize(ans, "integer"))

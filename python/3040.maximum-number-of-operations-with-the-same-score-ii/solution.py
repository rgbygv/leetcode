# Created by Jones at 2024/06/08 12:01
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/

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
    def maxOperations(self, nums: List[int]) -> int:
        """
        - `2 <= nums.length <= 2000`
        - `1 <= nums[i] <= 1000`
        """

        """
        we can try 
        - the 2 first
        - the 2 last
        - one first one last
        """

        @cache
        def dfs(l: int, r: int, target: int):
            if r - l + 1 < 2:
                return 0
            res = 0
            # op1
            if nums[l] + nums[l + 1] == target:
                res = 1 + dfs(l + 2, r, target)
            # op2
            if nums[r] + nums[r - 1] == target:
                res = max(res, 1 + dfs(l, r - 2, target))
            # op3
            if nums[l] + nums[r] == target:
                res = max(res, 1 + dfs(l + 1, r - 1, target))
            return res

        q = [nums[0] + nums[1], nums[-1] + nums[-2], nums[0] + nums[-1]]
        n = len(nums)
        return max(dfs(0, n - 1, target) for target in q)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxOperations(nums)
    print("\noutput:", serialize(ans, "integer"))

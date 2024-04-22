# Created by Jones at 2024/04/22 13:29
# leetgo: 1.4.5
# https://leetcode.cn/problems/combination-sum-iv/

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
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # - `1 <= nums.length <= 200`
        # - `1 <= nums[i] <= 1000`
        # - All the elements of `nums` are **unique**.
        # - `1 <= target <= 1000`

        nums.sort()

        @cache
        def dfs(target: int):
            if target == 0:
                return 1
            res = 0
            for x in nums:
                if (next_target := target - x) >= 0:
                    res += dfs(next_target)
                else:
                    break
            return res

        return dfs(target)

        # @cache
        # def dfs(i: int, target: int):
        #     """
        #     use only nums[..=i] to combine target, but no order

        #     """
        #     if target == 0:
        #         return 1
        #     if i == n:
        #         return 0
        #     res = 0
        #     # we sorted nums
        #     if nums[i] > target:
        #         return 0

        #     for t in count(0):
        #         if (next_target := target - nums[i] * t) >= 0:
        #             res += dfs(i + 1, next_target)
        #         else:
        #             break
        #     # print(i, target, res)
        #     return res

        # # print([dfs(i, target) for i in range(n)])
        # return sum(dfs(i, target) for i in range(n))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum4(nums, target)
    print("\noutput:", serialize(ans, "integer"))

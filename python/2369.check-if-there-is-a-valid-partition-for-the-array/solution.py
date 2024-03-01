# Created by Jones at 2024/03/01 11:08
# leetgo: 1.4.1
# https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/

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
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def dfs(i: int):
            if i == 0:
                return False
            if i == 1:
                return nums[i] == nums[i - 1]
            if i == 2:
                return (
                    nums[i] == nums[i - 1] == nums[i - 2]
                    or nums[i] == nums[i - 1] + 1
                    and nums[i - 1] == nums[i - 2] + 1
                )

            if nums[i] == nums[i - 1] and dfs(i - 2):
                return True
            if nums[i] == nums[i - 1] == nums[i - 2] and dfs(i - 3):
                return True
            if (
                nums[i] == nums[i - 1] + 1
                and nums[i - 1] == nums[i - 2] + 1
                and dfs(i - 3)
            ):
                return True
            return False

        return dfs(n - 1)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))

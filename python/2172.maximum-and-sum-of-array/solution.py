# Created by Jones at 2024/04/25 14:45
# leetgo: 1.4.5
# https://leetcode.cn/problems/maximum-and-sum-of-array/

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
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        # - `n == nums.length`
        # - `1 <= numSlots <= 9`
        # - `1 <= n <= 2 * numSlots`
        # - `1 <= nums[i] <= 15`

        n = len(nums)

        # O(n * numslots * (1 << (2*numslots)))
        @cache
        def dfs(i: int, mask: int):
            """nums[i], mask show we have used how many of numSlots"""
            # print(i, mask)
            if i == n:
                return 0
            # we use two bits to replace one slots, 00 and 01 is valid
            res = 0
            for d in range(numSlots):
                d *= 2  # use 2 bits
                cur = mask >> d
                if cur & 0b10 == 0:
                    res = max(
                        res,
                        (nums[i] & (d // 2 + 1))
                        + dfs(i + 1, ((cur + 1) << d) + (mask & ((1 << d) - 1))),
                    )
            return res

        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    numSlots: int = deserialize("int", read_line())
    ans = Solution().maximumANDSum(nums, numSlots)
    print("\noutput:", serialize(ans, "integer"))

# Created by Jones at 2024/05/20 13:54
# leetgo: 1.4.7
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

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
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        - `1 <= nums.length <= 12`
        - `1 <= nums[i] <= 20`
        """
        res = 0
        n = len(nums)
        for mask in range(1 << n):
            cur = 0
            for i in range(n):
                if mask >> i & 1:
                    cur ^= nums[i]
            res += cur
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsetXORSum(nums)
    print("\noutput:", serialize(ans, "integer"))

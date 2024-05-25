# Created by Jones at 2024/05/25 13:27
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-indices-with-index-and-value-difference-i/

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
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        for i, x in enumerate(nums):
            for j in range(i + indexDifference, len(nums)):
                if abs(x - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1, -1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    indexDifference: int = deserialize("int", read_line())
    valueDifference: int = deserialize("int", read_line())
    ans = Solution().findIndices(nums, indexDifference, valueDifference)
    print("\noutput:", serialize(ans, "integer[]"))

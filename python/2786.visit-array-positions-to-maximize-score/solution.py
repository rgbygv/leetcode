# Created by Jones at 2024/06/14 13:15
# leetgo: 1.4.7
# https://leetcode.cn/problems/visit-array-positions-to-maximize-score/

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
    def maxScore(self, nums: List[int], x: int) -> int:
        """
        **Note** that initially you have `nums[0]` points.
        if nums[i] & 1:
            odd[i] =nums[i] +  max(odd[i-1], even[i-1] -x )
        else:
            ...
        """
        odd = even = nums[0]
        if nums[0] & 1:
            even -= x
        else:
            odd -= x

        for i in range(1, len(nums)):
            score = nums[i]
            if score & 1:
                odd = score + max(odd, even - x)
            else:
                even = score + max(even, odd - x)

        return max(odd, even)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().maxScore(nums, x)
    print("\noutput:", serialize(ans, "long"))

# Created by Jones at 2024/05/31 09:05
# leetgo: 1.4.7
# https://leetcode.com/problems/single-number-iii/

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
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        if this two number is x,y
        then x^y = xor(nums)
        if any bit of (x^y) is 1
        then x[bit] is diff y[bit], we can divide nums by it
        """
        xy = reduce(xor, nums)
        lowbit = xy & (-xy)
        x, y = 0, 0
        for num in nums:
            if num & lowbit != 0:
                x ^= num
            else:
                y ^= num
        return [x, y]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)
    print("\noutput:", serialize(ans, "integer[]"))

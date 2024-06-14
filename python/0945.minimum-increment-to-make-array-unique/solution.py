# Created by Jones at 2024/06/14 13:26
# leetgo: 1.4.7
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

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
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        - `1 <= nums.length <= 10⁵`
        - `0 <= nums[i] <= 10⁵`
        """
        nums.sort()
        res = 0
        last = -1

        for x in nums:
            if x <= last:
                res += last + 1 - x
                last += 1
            else:
                last = x
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minIncrementForUnique(nums)
    print("\noutput:", serialize(ans, "integer"))

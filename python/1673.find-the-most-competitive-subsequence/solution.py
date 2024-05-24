# Created by Jones at 2024/05/24 10:18
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-most-competitive-subsequence/

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
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        - `1 <= nums.length <= 10⁵`
        - `0 <= nums[i] <= 10⁹`
        - `1 <= k <= nums.length`
        """

        """
        we should try to use the smallest number as first
        """
        n = len(nums)
        st = []
        for i, x in enumerate(nums):
            # try use x as top
            while st and x < st[-1] and (len(st) - 1 + n - i) >= k:
                st.pop()
            st.append(x)
        return st[:k]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().mostCompetitive(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))

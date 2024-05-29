# Created by Jones at 2024/05/29 13:57
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-subarray-min-product/

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
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        # find the border of the nums[i]
        left = [0] * n
        right = [n - 1] * n
        st = []
        for i, x in enumerate(nums):
            while st and x < nums[st[-1]]:
                right[st.pop()] = i - 1
            if st:
                left[i] = st[-1] + 1
            st.append(i)
        p = list(accumulate(nums, initial=0))
        res = 0
        for i, x in enumerate(nums):
            l = left[i]
            r = right[i]
            res = max(res, x * (p[r + 1] - p[l]))
        return res % mod


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSumMinProduct(nums)
    print("\noutput:", serialize(ans, "integer"))

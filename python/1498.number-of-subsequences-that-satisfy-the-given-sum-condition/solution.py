# Created by Jones at 2024/05/07 13:53
# leetgo: 1.4.6
# https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

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
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0

        def calc(size: int):
            return pow(2, size, mod)

        while l <= r:
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
            if l > r:
                break
            res += calc(r - l)
            res %= mod
            l += 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numSubseq(nums, target)
    print("\noutput:", serialize(ans, "integer"))

# Created by Jones at 2024/05/08 14:57
# leetgo: 1.4.6
# https://leetcode.cn/problems/make-sum-divisible-by-p/

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
    def minSubarray(self, nums: List[int], p: int) -> int:
        if p == 1:
            return 0
        # we should find a subarray sum(..) % p == target
        target = sum(nums) % p
        if target == 0:
            return 0
        mp = {0: 0}
        s = 0
        res = len(nums)
        for i, x in enumerate(nums, 1):
            s = (s + x) % p
            # find largest j < i that (s[i] - s[j]) % p == target
            # => s[j] % p == (s[i] -target) % p
            if (pre := (s - target) % p) in mp:
                # ic(target, pre, i, s)
                res = min(res, i - mp[pre])
            mp[s] = i

        if res >= len(nums):
            return -1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    p: int = deserialize("int", read_line())
    ans = Solution().minSubarray(nums, p)
    print("\noutput:", serialize(ans, "integer"))

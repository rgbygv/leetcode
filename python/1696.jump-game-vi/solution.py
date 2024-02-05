# Created by Jones at 2024/02/05 12:56
# leetgo: 1.4.1
# https://leetcode.cn/problems/jump-game-vi/

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
    def maxResult(self, nums: List[int], k: int) -> int:
        # f[i] = max(f[i-k:i]) + nums[i]
        q = []
        n = len(nums)
        f = nums[:]
        for i, x in enumerate(nums):
            while q and q[0][1] + k < i:
                heappop(q)
            if q:
                f[i] -= q[0][0]
            heappush(q, (-f[i], i))
        # print(f)
        return f[-1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxResult(nums, k)
    print("\noutput:", serialize(ans, "integer"))

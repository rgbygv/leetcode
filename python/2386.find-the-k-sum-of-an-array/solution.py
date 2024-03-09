# Created by Jones at 2024/03/09 22:47
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-k-sum-of-an-array/

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
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0
        for i in range(n):
            if nums[i] > 0:
                s += nums[i]
            else:
                nums[i] = -nums[i]
        nums.sort()

        q = [(0, 0)]
        for _ in range(k - 1):
            cur, i = heappop(q)
            if i < len(nums):
                heappush(q, (cur + nums[i], i + 1))
                if i:
                    heappush(q, (cur + nums[i] - nums[i - 1], i + 1))
        return s - q[0][0]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kSum(nums, k)
    print("\noutput:", serialize(ans, "long"))

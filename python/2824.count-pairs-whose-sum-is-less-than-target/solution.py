# Created by Jones at 2023/11/24 16:11
# leetgo: dev
# https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        n = len(nums)
        r = n - 1

        res = 0
        while l < r:
            if nums[l] + nums[r] < target:
                res += r - l
                l += 1
            else:
                r -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().countPairs(nums, target)

    print("\noutput:", serialize(ans))

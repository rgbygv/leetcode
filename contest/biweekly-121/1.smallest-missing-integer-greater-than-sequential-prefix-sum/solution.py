# Created by Jones at 2024/01/06 22:30
# leetgo: dev
# https://leetcode.cn/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# https://leetcode.cn/contest/biweekly-contest-121/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

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


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
                i += 1
            else:
                break

        seen = set(nums)
        while s in seen:
            s += 1
        return s


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().missingInteger(nums)

    print("\noutput:", serialize(ans))

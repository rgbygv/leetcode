# Created by Jones at 2024/03/14 13:07
# leetgo: 1.4.2
# https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/

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
    def maxArrayValue(self, nums: List[int]) -> int:
        res = -inf
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] <= res:
                res += nums[i]
            else:
                res = nums[i]
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArrayValue(nums)
    print("\noutput:", serialize(ans, "long"))

# Created by Jones at 2024/01/31 14:15
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-distinct-difference-array/

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
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [0] * (n + 1)

        seen = set()
        for i in reversed(range(n)):
            seen.add(nums[i])
            suf[i] = len(seen)
        seen.clear()
        res = [0] * n
        for i, x in enumerate(nums):
            seen.add(x)
            res[i] = len(seen) - suf[i + 1]
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().distinctDifferenceArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))

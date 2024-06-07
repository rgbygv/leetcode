# Created by Jones at 2024/06/07 12:35
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-i/

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
    def maxOperations(self, nums: List[int]) -> int:
        s = nums[0] + nums[1]
        res = 0
        for i in range(0, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] == s:
                res += 1
            else:
                break

        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxOperations(nums)
    print("\noutput:", serialize(ans, "integer"))

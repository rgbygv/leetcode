# Created by Jones at 2024/05/18 08:17
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-maximum-divisibility-score/

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
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res, cnt = 0, -1
        for d in divisors:
            cur = sum(x % d == 0 for x in nums)
            if cur > cnt or cur == cnt and d < res:
                cnt = cur
                res = d
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    divisors: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDivScore(nums, divisors)
    print("\noutput:", serialize(ans, "integer"))

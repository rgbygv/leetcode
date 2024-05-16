# Created by Jones at 2024/05/16 15:07
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/

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
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        s = sum(milestones)
        if (s - milestones[-1]) >= milestones[-1] - 1:
            return s
        return (s - milestones[-1]) * 2 + 1


# @lc code=end

if __name__ == "__main__":
    milestones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfWeeks(milestones)
    print("\noutput:", serialize(ans, "long"))

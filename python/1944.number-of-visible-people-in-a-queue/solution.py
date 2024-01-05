# Created by Bob at 2024/01/05 15:21
# leetgo: dev
# https://leetcode.cn/problems/number-of-visible-people-in-a-queue/

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
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """ """
        n = len(heights)

        st = []
        res = [0] * n

        for i, x in enumerate(heights):
            while st and x > heights[st[-1]]:
                res[st.pop()] += 1
            if st:
                res[st[-1]] += 1
            st.append(i)

        return res


# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canSeePersonsCount(heights)

    print("\noutput:", serialize(ans))

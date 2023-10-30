# Created by Jones at 2023/10/30 19:50
# leetgo: dev
# https://leetcode.cn/problems/h-index-ii/

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
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        if citations[-1] == 0:
            return 0

        l = 1
        r = n

        while l <= r:
            mid = (l + r) >> 1
            if citations[n - mid] >= mid:
                l = mid + 1
            else:
                r = mid - 1

        return r


# @lc code=end

if __name__ == "__main__":
    citations: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hIndex(citations)

    print("\noutput:", serialize(ans))

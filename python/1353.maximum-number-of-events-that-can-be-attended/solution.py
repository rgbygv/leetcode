# Created by Jones at 2024/05/06 21:12
# leetgo: 1.4.6
# https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/

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
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        q = []
        res = 0
        i = 0
        for t in range(1, 10**5 + 1):
            while i < n and events[i][0] == t:
                heappush(q, events[i][1])
                i += 1
            while q and q[0] < t:
                heappop(q)
            if q:
                res += 1
                heappop(q)
        return res

        return 0


# @lc code=end

if __name__ == "__main__":
    events: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxEvents(events)
    print("\noutput:", serialize(ans, "integer"))

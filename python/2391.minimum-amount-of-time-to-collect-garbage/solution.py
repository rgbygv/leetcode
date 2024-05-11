# Created by Jones at 2024/05/11 09:33
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/

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
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        """
        - `2 <= garbage.length <= 10⁵`
        - `garbage[i]` consists of only the letters `'M'`, `'P'`, and `'G'`.
        - `1 <= garbage[i].length <= 10`
        - `travel.length == garbage.length - 1`
        - `1 <= travel[i] <= 100`
        """

        res = 0
        last = {}

        for i, each in enumerate(garbage):
            res += len(each)
            for ch in set(each):
                last[ch] = i

        p = list(accumulate(travel, initial=0))
        for ch, i in last.items():
            res += p[i]

        return res


# @lc code=end

if __name__ == "__main__":
    garbage: List[str] = deserialize("List[str]", read_line())
    travel: List[int] = deserialize("List[int]", read_line())
    ans = Solution().garbageCollection(garbage, travel)
    print("\noutput:", serialize(ans, "integer"))

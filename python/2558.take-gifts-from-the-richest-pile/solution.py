# Created by Jones at 2023/10/28 13:09
# leetgo: dev
# https://leetcode.cn/problems/take-gifts-from-the-richest-pile/

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
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = [-x for x in gifts]

        heapify(q)

        for _ in range(k):
            x = -heappop(q)
            if x == 1:
                return len(gifts)
            heappush(q, -isqrt(x))

        return -sum(q)


# @lc code=end

if __name__ == "__main__":
    gifts: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().pickGifts(gifts, k)

    print("\noutput:", serialize(ans))

# Created by Jones at 2023/11/02 13:51
# leetgo: dev
# https://leetcode.cn/problems/rings-and-rods/

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
    def countPoints(self, rings: str) -> int:
        cnt = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            ring = int(rings[i + 1])
            cnt[ring].add(rings[i])

        return sum(1 for i in range(10) if len(cnt[i]) == 3)


# @lc code=end

if __name__ == "__main__":
    rings: str = deserialize("str", read_line())
    ans = Solution().countPoints(rings)

    print("\noutput:", serialize(ans))

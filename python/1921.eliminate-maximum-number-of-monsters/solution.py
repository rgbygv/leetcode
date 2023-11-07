# Created by Jones at 2023/11/07 14:56
# leetgo: dev
# https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/

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
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrive = [(x + y - 1) // y for x, y in zip(dist, speed)]
        arrive.sort()
        for i, x in enumerate(arrive, 1):
            if x < i:
                return i - 1
        return len(dist)


# @lc code=end

if __name__ == "__main__":
    dist: List[int] = deserialize("List[int]", read_line())
    speed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().eliminateMaximum(dist, speed)

    print("\noutput:", serialize(ans))

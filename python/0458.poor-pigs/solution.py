# Created by Jones at 2023/10/29 12:33
# leetgo: dev
# https://leetcode.cn/problems/poor-pigs/

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
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie
        x = 0
        while pow(t + 1, x) < buckets:
            x += 1
        return x


# @lc code=end

if __name__ == "__main__":
    buckets: int = deserialize("int", read_line())
    minutesToDie: int = deserialize("int", read_line())
    minutesToTest: int = deserialize("int", read_line())
    ans = Solution().poorPigs(buckets, minutesToDie, minutesToTest)

    print("\noutput:", serialize(ans))

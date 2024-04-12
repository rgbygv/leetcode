# Created by Jones at 2024/04/12 12:58
# leetgo: 1.4.5
# https://leetcode.cn/problems/find-champion-i/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        can = [True] * n
        for row in grid:
            for j, x in enumerate(row):
                if x == 1:
                    can[j] = False
        return can.index(True)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findChampion(grid)
    print("\noutput:", serialize(ans, "integer"))

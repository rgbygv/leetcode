# Created by Jones at 2023/12/17 14:14
# leetgo: dev
# https://leetcode.cn/problems/find-missing-and-repeated-values/
# https://leetcode.cn/contest/weekly-contest-376/problems/find-missing-and-repeated-values/

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
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cnt = Counter()
        n = len(grid)
        for i, row in enumerate(grid):
            for x in row:
                cnt[x] += 1

        dup = miss = -1
        for i in range(1, n * n + 1):
            if cnt[i] == 2:
                dup = i
            elif cnt[i] == 0:
                miss = i
        return [dup, miss]


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMissingAndRepeatedValues(grid)

    print("\noutput:", serialize(ans))

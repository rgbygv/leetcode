# Created by Jones at 2023/12/17 14:10
# leetgo: dev
# https://leetcode.cn/problems/min-cost-climbing-stairs/

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
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dfs(i: int):
            if i <= 1:
                return 0
            return min(cost[i - 1] + dfs(i - 1), cost[i - 2] + dfs(i - 2))

        return dfs(n)


# @lc code=end

if __name__ == "__main__":
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCostClimbingStairs(cost)

    print("\noutput:", serialize(ans))

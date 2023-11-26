# Created by Jones at 2023/11/25 22:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/
# https://leetcode.cn/contest/biweekly-contest-118/problems/minimum-number-of-coins-for-fruits/

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
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, rest: int):
            if i == n:
                return 0
            if rest == 0:
                return prices[i] + dfs(i + 1, i + 1)

            return min(dfs(i + 1, rest - 1), prices[i] + dfs(i + 1, i + 1))

        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCoins(prices)

    print("\noutput:", serialize(ans))

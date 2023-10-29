# Created by Jones at 2023/10/29 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/
# https://leetcode.cn/contest/weekly-contest-369/problems/maximum-points-after-collecting-coins-from-all-nodes/

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
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)

        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        @cache
        def dfs(x: int, fa: int, state: int):
            if (1 << state) > 10**4:
                return 0
            op1 = (
                coins[x] // pow(2, state)
                - k
                + sum(dfs(y, x, state) for y in g[x] if y != fa)
            )

            op2 = coins[x] // pow(2, state + 1) + sum(
                dfs(y, x, state + 1) for y in g[x] if y != fa
            )

            return max(op1, op2)

        return dfs(0, -1, 0)


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    coins: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumPoints(edges, coins, k)

    print("\noutput:", serialize(ans))

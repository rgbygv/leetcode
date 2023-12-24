# Created by Jones at 2023/12/24 22:16
# leetgo: dev
# https://leetcode.cn/problems/minimum-cost-to-convert-string-i/
# https://leetcode.cn/contest/weekly-contest-377/problems/minimum-cost-to-convert-string-i/

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
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        N = 26
        g = [[inf] * N for _ in range(N)]

        for x, y, c in zip(original, changed, cost):
            x = ord(x) - ord("a")
            y = ord(y) - ord("a")
            g[x][y] = min(g[x][y], c)

        seen = {}

        def helper(X):
            X = ord(X) - ord("a")
            if X not in seen:
                dist = [inf] * N
                dist[X] = 0

                q = [(0, X)]
                while q:
                    d, x = heappop(q)
                    for y, c in enumerate(g[x]):
                        if d + c < dist[y]:
                            dist[y] = d + c
                            heappush(q, (dist[y], y))
                seen[X] = dist

            return seen[X]

        res = 0
        for x, y in zip(source, target):
            if x == y:
                continue
            v = helper(x)
            # print(x, v)
            y = ord(y) - ord("a")
            if v[y] == inf:
                return -1
            res += v[y]
        return res


# @lc code=end

if __name__ == "__main__":
    source: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    original: List[str] = deserialize("List[str]", read_line())
    changed: List[str] = deserialize("List[str]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(source, target, original, changed, cost)

    print("\noutput:", serialize(ans))

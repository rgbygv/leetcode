# Created by Jones at 2023/11/14 19:55
# leetgo: dev
# https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

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
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        res = cnt = inf
        for i in range(n):
            q = [(0, i)]
            dist = [inf] * n
            dist[i] = 0
            while q:
                d, x = heappop(q)
                for y, w in g[x]:
                    nd = d + w
                    if nd < dist[y] and nd <= distanceThreshold:
                        dist[y] = nd
                        heappush(q, (nd, y))
            cur = sum(x <= distanceThreshold for x in dist) - 1
            if cur <= cnt:
                cnt = cur
                res = i
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    distanceThreshold: int = deserialize("int", read_line())
    ans = Solution().findTheCity(n, edges, distanceThreshold)

    print("\noutput:", serialize(ans))

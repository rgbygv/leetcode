# Created by Jones at 2023/11/12 22:22
# leetgo: dev
# https://leetcode.cn/problems/bus-routes/

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
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        mp = defaultdict(list)
        for i, route in enumerate(routes):
            ok1 = ok2 = False
            for x in route:
                mp[x].append(i)
                if x == source:
                    ok1 = True
                elif x == target:
                    ok2 = True
            if ok1 and ok2:
                return 1
        n = len(routes)
        dist = [inf] * n
        q = mp[source].copy()
        mp[source].clear()
        if not q:
            return -1
        for x in q:
            dist[x] = 1

        while q:
            nxt = []
            for x in q:
                for y in routes[x]:
                    for z in mp[y]:
                        if dist[z] == inf:
                            dist[z] = dist[x] + 1
                            nxt.append(z)
                        if y == target:
                            return dist[z]
                    mp[y].clear()
            q = nxt
        return -1

        # g = defaultdict(list)
        # for route in routes:
        #     for x, y in pairwise(route):
        #         g[x].append(y)
        #     g[route[-1]].append(route[0])

        # dist = defaultdict(lambda: inf)

        # q = [(0, source)]
        # while q:
        #     d, x = heappop(q)
        #     if x == target:
        #         return d
        #     for y in g[x]:
        #         if d + 1 < dist[y]:
        #             dist[y] = d + 1
        #             heappush(q, (dist[y], y))
        # return -1


# @lc code=end

if __name__ == "__main__":
    routes: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numBusesToDestination(routes, source, target)

    print("\noutput:", serialize(ans))

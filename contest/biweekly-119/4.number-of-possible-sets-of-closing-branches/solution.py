# Created by Jones at 2023/12/09 22:30
# leetgo: dev
# https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/
# https://leetcode.cn/contest/biweekly-contest-119/problems/number-of-possible-sets-of-closing-branches/

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
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        res = 0
        g = {}
        for x, y, w in roads:
            if x > y:
                x, y = y, x
            e = (x, y)
            if e not in g:
                g[e] = w
            else:
                g[e] = min(g[e], w)

        edge = [[] for _ in range(n)]
        for (x, y), w in g.items():
            edge[x].append((y, w))
            edge[y].append((x, w))
        res = 0
        for mask in range(1 << n):
            tmp = [inf] * n
            q = []
            for i in range(n):
                if mask >> i & 1:
                    tmp[i] = -inf
                    continue
                q.append(i)

            def check(q):
                for x in q:
                    dist = tmp[:]
                    dist[x] = 0
                    dq = deque([(x, -1)])
                    while dq:
                        x, fa = dq.popleft()
                        for y, w in edge[x]:
                            if y == fa or dist[y] == -inf:
                                continue
                            if dist[x] + w < dist[y]:
                                dist[y] = dist[x] + w
                                dq.append((y,x))
                    for y in dist:
                        if y > maxDistance:
                            return False
                return True

            res += check(q)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    maxDistance: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberOfSets(n, maxDistance, roads)

    print("\noutput:", serialize(ans))

# Created by Jones at 2023/12/05 14:36
# leetgo: dev
# https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/

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
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        if n == 1:
            return 0
        g = [[] for _ in range(n)]
        deg = [0] * n

        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = deque(i for i, d in enumerate(deg) if d == 1)
        if q[0] == 0:
            q.popleft()

        size = [1] * n
        res = 0
        while q:
            x = q.popleft()
            deg[x] = 0  # tag visited
            for y in g[x]:
                if deg[y] == 0:
                    continue
                size[y] += size[x]
                res += (size[x] + seats - 1) // seats
                deg[y] -= 1
                if y != 0 and deg[y] == 1:
                    q.append(y)

        # print(size)
        return res


# @lc code=end

if __name__ == "__main__":
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    seats: int = deserialize("int", read_line())
    ans = Solution().minimumFuelCost(roads, seats)

    print("\noutput:", serialize(ans))

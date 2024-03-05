# Created by Jones at 2024/03/05 19:01
# leetgo: 1.4.1
# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/

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
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7

        g = [[] for _ in range(n)]

        for x, y, t in roads:
            g[x].append((y, t))
            g[y].append((x, t))

        dist = [inf] * n
        dist[0] = 0
        f = [1] * n  # count

        q = [(0, 0)]
        while q:
            d, x = heappop(q)
            for y, t in g[x]:
                if dist[y] > d + t:
                    dist[y] = d + t
                    heappush(q, (dist[y], y))
                    f[y] = f[x]
                elif dist[y] == d + t:
                    f[y] += f[x]
        return f[n - 1] % mod


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, roads)
    print("\noutput:", serialize(ans, "integer"))

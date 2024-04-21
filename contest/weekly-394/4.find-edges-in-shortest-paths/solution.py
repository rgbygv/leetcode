# Created by Jones at 2024/04/21 13:16
# leetgo: 1.4.5
# https://leetcode.cn/problems/find-edges-in-shortest-paths/
# https://leetcode.cn/contest/weekly-contest-394/problems/find-edges-in-shortest-paths/

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
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (x, y, w) in enumerate(edges):
            g[x].append((y, w, i))
            g[y].append((x, w, i))

        dist = [inf] * n
        dist[0] = 0
        f = [[] for _ in range(n)]

        q = [(0, 0)]
        while q:
            dx, x = heappop(q)
            print(dx, x)
            if x == n - 1:
                continue
            for y, w, i in g[x]:
                if (d := dx + w) <= dist[y]:
                    # find a new min path
                    if d < dist[y]:
                        heappush(q, (d, y))
                        f[y].clear()
                    f[y].append((i, x))
                    dist[y] = d
        res = [False] * len(edges)
        vis = [False] * n

        def dfs(x: int):
            if vis[x]:
                return
            vis[x] = True
            for i, y in f[x]:
                res[i] = True
                dfs(y)

        # print(f)
        dfs(n - 1)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findAnswer(n, edges)
    print("\noutput:", serialize(ans, "boolean[]"))

# Created by Jones at 2024/05/15 20:15
# leetgo: 1.4.7
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional


# @lc code=begin
class UnionFind:
    def __init__(self, n) -> None:
        self.components = n
        self.fa = list(range(n))
        self.rank = [1] * n

    def __str__(self) -> str:
        return " ".join(map(str, self.fa))

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.rank[fy] > self.rank[fx]:
            fx, fy = fy, fx
        self.fa[fy] = fx
        self.rank[fx] += self.rank[fy]
        self.components -= 1
        return True

    def merge(self, x, y):
        fx, fy = self.find(x), self.find(y)
        self.rank[fy] += self.rank[fx]
        self.fa[fx] = fy

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def all_is_connected(self):
        return self.components == 1

    def size(self, x):
        return self.rank[self.find(x)]


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        - `1 <= grid.length == n <= 400`
        - `grid[i].length == n`
        - `grid[i][j]` is either `0` or `1`.
        - There is at least one thief in the `grid`.
        """
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        q = []

        dist = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0
        g = [q]
        while q:
            nxt = []
            for x, y in q:
                for dx, dy in pairwise((0, 1, 0, -1, 0)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] < 0:
                        dist[nx][ny] = dist[x][y] + 1
                        nxt.append((nx, ny))
            q = nxt
            g.append(q)

        uf = UnionFind(m * n + 1)
        for d in range(len(g) - 2, 0, -1):
            for x, y in g[d]:
                for dx, dy in pairwise((0, 1, 0, -1, 0)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] >= d:
                        uf.union(x * n + y, nx * n + ny)
            if uf.is_connected(0, m * n - 1):
                return d
        return 0


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumSafenessFactor(grid)
    print("\noutput:", serialize(ans, "integer"))

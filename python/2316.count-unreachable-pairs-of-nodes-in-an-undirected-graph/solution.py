# Created by Jones at 2023/10/21 14:55
# leetgo: dev
# https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)

        cnt = Counter()

        for x in range(n):
            cnt[uf.find(x)] += 1

        pre = 0
        res = 0
        for c in cnt.values():
            res += pre * c
            pre += c
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPairs(n, edges)

    print("\noutput:", serialize(ans))
